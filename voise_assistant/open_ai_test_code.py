import os
from gpt4all import GPT4All

model_path = r"C:\Users\yehor\AppData\Local\nomic.ai\GPT4All\Llama-3.2-1B-Instruct-Q4_0.gguf"

# Проверяем, существует ли файл модели
if not os.path.exists(model_path):
    raise FileNotFoundError(f"❌ Модель не найдена по пути: {model_path}")

# Загружаем модель
local_model = GPT4All(model_path)

class LocalModel:
    def __init__(self):
        self.model = local_model
    
    def generate_response(self, message):
        return self.model.generate(message)

# Test model
model = LocalModel()
response = model.generate_response("Hello! How are you?")
print("🤖 AI:", response)
