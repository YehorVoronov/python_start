from __future__ import annotations
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    WorkerOptions,
    cli,
)
from livekit.agents.multimodal import MultimodalAgent
from dotenv import load_dotenv
from api import AssistantFnc
from prompts import WELCOME_MESSAGE
import os
from gpt4all import GPT4All

load_dotenv()

# Load local AI model (GPT4All)
model_path = r"C:\Users\yehor\AppData\Local\nomic.ai\GPT4All\Llama-3.2-1B-Instruct-Q4_0.gguf"

if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Model not found at: {model_path}")

local_model = GPT4All(model_path, device="cpu")

class LocalModel:
    def __init__(self):
        self.model = local_model
    
    def generate_response(self, message):
        return self.model.generate(message)
    
    @property
    def session(self):
        class DummySession:
            def __init__(self):
                self.conversation = self
                self.response = self
                self._init_sync_task = self._dummy_coroutine()  # ✅ Awaitable coroutine
                self.event_handlers = {}  # ✅ Store event handlers

            async def _dummy_coroutine(self):
                return None  # ✅ Fix: Makes _init_sync_task awaitable

            def item(self):
                return self
            
            def create(self, message):
                print("Simulating AI response:", message.content)

            def on(self, event_name, callback, *args, **kwargs):  # ✅ Accepting *args and **kwargs
                # Debugging to check the callback
                print(f"Registering event: {event_name} with callback: {callback}")
                if callable(callback):
                    self.event_handlers[event_name] = (callback, args, kwargs)  # Store with arguments
                    print(f"✅ Event listener registered for: {event_name} with {callback}")
                else:
                    print(f"❌ Callback is not callable for event: {event_name}")

        return DummySession()


# Custom wrapper for integration with MultimodalAgent
class LocalAIWrapper:
    def __init__(self, model):
        self.model = model
    
    async def generate(self, prompt, **kwargs):
        return self.model.generate_response(prompt)

    # Update session() to accept keyword arguments
    def session(self, *args, **kwargs):
        return self.model.session  # Returning the dummy session from LocalModel

async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)
    await ctx.wait_for_participant()

    # Use local GPT4All model instead of OpenAI
    model_wrapper = LocalAIWrapper(LocalModel())
    assistant_fnc = AssistantFnc()
    assistant = MultimodalAgent(model=model_wrapper, fnc_ctx=assistant_fnc)
    assistant.start(ctx.room)

    # Send initial message
    print("🤖 AI:", model_wrapper.generate(WELCOME_MESSAGE))

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
