import ollama
from ollama import chat
from ollama_ocr import OCRProcessor

llm = 'llama3.2-vision:11b'

def explain(path):
    response = ollama.chat(
        model=llm, 
        messages=[{
            'role': 'user',
            'content': 'Can you explain what wine is on this image, and the quality?',
            'images': [path]
        }]
    )
    return response.message.content