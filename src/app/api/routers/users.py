from fastapi import APIRouter, HTTPException
from app.api.shared.llm_deps import send_message_to_llm
from app.schemas.chat import ChatCreate

router = APIRouter()

@router.post("/send_message")
async def send_message(
    chat: ChatCreate
):
    try:
        response = send_message_to_llm(message=chat.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending message to LLM: {str(e)}")