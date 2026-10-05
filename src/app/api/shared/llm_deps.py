from groq import Groq
from fastapi import HTTPException
from app.core.config import settings

def get_client() -> Groq:
    """
    Returns an instance of Groq client initialized with the provided API key."""
    client = Groq(api_key=settings.LLM_API_KEY, timeout=30)
    return client

def send_message_to_llm(message: str = ""):
    """
    Sends a message to the LLM API and returns the response.
    """
    try:
        client = get_client()
        completion = client.chat.completions.create(
            model="qwen/qwen3.8-27b",
            messages=[
            {
                "role": "user",
                "content": message
            }
            ],
            temperature=1,
            max_completion_tokens=2048,
            top_p=1
        )
        assistant_message = completion.choices[0].message
        return {
            "reply": assistant_message.content,
            "model": completion.model,
            "role": assistant_message.role
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with LLM API: {str(e)}")
