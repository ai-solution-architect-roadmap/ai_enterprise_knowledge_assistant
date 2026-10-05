from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import text
from app.api.routers.router import router as api_router
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import get_db

app = FastAPI()

app.include_router(api_router)

@app.get("/health")
async def health_check(
    db: Annotated[AsyncSession, Depends(get_db)]
):
    try:
        # Perform a simple query to check if database connection if fine
        await db.execute(text("SELECT 1"))
    except SQLAlchemyError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Database connection error"
        ) from exc

    return {"status": "Welcome! to the AI Knowledge assistant. All services are running smoothly!"}
