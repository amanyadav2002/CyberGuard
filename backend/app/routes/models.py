from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from app.ml.model_manager import model_manager

router = APIRouter(prefix="/api/models", tags=["models"])

class ModelSelectRequest(BaseModel):
    model_name: str

@router.get("/active")
def get_active_model():
    return {"active_model": model_manager.active_model_name}

@router.post("/select")
def select_model(request: ModelSelectRequest):
    success = model_manager.set_active_model(request.model_name)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Model '{request.model_name}' is not supported by the platform."
        )
    return {"active_model": model_manager.active_model_name, "message": f"Successfully loaded {request.model_name}"}
