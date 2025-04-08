import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("OPENAI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

def generate_comedy_text(task_description):
    try:
        response = model.generate_content(
            f"Make a short, witty, and funny one-liner about this task: '{task_description}'"
        )
        return response.text.strip()
    except Exception as e:
        return f"(AI error: {e})"

