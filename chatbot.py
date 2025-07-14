from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os

api_key = os.getenv("GEMINI_API_KEY")

def generate_answer(user_input):
    prompt = f"You are a helpful AI interview coach. Analyze the student's answer: '{user_input}'. Give feedback with pros, cons, and suggestions to improve."
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error from Gemini: {e}"
