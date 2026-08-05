from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.database import init_db
from app.ml.model_manager import model_manager
from app.routes import auth, models, scan, reports

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Init db tables and train/cache ML models
    init_db()
    model_manager.initialize_all_models()
    yield
    # Shutdown: No resources to release
    pass

app = FastAPI(
    title="CyberGuard Platform API",
    description="Backend threat scoring pipeline for URLs and Android APK components.",
    version="1.0.0",
    lifespan=lifespan
)

# CORS Policy
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router Registrations
app.include_router(auth.router)
app.include_router(models.router)
app.include_router(scan.router)
app.include_router(reports.router)

@app.get("/")
def read_root():
    return {
        "status": "ONLINE",
        "service": "CyberGuard Threat Intelligence API Gateway",
        "active_model": model_manager.active_model_name
    }
