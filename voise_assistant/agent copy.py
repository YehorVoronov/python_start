from __future__ import annotations
from livekit.agents import (
 AutoSubscribe,
 JobContext,
 WorkerOptions,
 cli,
 llm
)
from livekit.agents.multimodal import MultimodalAgent
from livekit.plugins import openai
from dotenv import load_dotenv
from api import AssistantFnc
from prompts import WELCOME_MESSAGE, INSTRUCTIONS
import os

load_dotenv()

async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.SUBSCRIBE_ALL)
    await ctx.wait_for_participant()

    model = openai.realtime.RealtimeModel(
        instructions=INSTRUCTIONS,
        voice="shimmer",
        temperature=0.8,
        modalities=["audio","text"]
    )
    assistant_fnc = AssistantFnc()
    # assistant = MultimodalAgent(model= model, fnc_ctx=assistant_fnc)
    class CustomAssistant:
        def __init__(self, model):
         self.model = model

        def respond(self, message):
            return self.model.generate_response(message)

    assistant = CustomAssistant(model)

    assistant.start(ctx.room)

    # seession = model.session[0]
    # seession.conversation.item.create(
    #     llm.ChatMessage(
    #         role = "assistant",
    #         content = WELCOME_MESSAGE
    #     )
    # )
    # seession.response.create()
    # Send welcome message using local AI
    print("🤖 AI:", assistant.respond(WELCOME_MESSAGE))


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))


