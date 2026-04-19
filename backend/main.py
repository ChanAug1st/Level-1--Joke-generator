# Create a FastAPI POST endpoint "/generate"
# Define a Pydantic model with fields: theme (str), type (str)
# The endpoint should accept JSON input
# Return a JSON response with a "result" field


from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from google import genai


load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()

# ===== CORS =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===== request model =====
class GenerateRequest(BaseModel):
    theme: str
    type: str

@app.post("/generate")
def generate(req: GenerateRequest):

    prompt = f"""
    You are a professional comedian specializing in {req.theme} humor.

    Your task is to generate a high-quality {req.type}.

    Requirements:
    - Theme: {req.theme}
    - Type: {req.type}

    If the type is "joke":
    - Keep it under 80 words
    - Include a clear punchline

    If the type is "story":
    - Keep it under 150 words
        - Include a beginning, middle, and end

    Output:
    Return only the final result.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {"result": response.text}
