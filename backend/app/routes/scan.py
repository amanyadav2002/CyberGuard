import os
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException, status
from pydantic import BaseModel
from app.utils.url_extractor import extract_url_features
from app.utils.apk_extractor import extract_apk_features
from app.ml.model_manager import model_manager
from app.database import log_scan

router = APIRouter(prefix="/api/scan", tags=["scan"])

class URLScanRequest(BaseModel):
    url: str

@router.post("/url")
def scan_url(request: URLScanRequest):
    if not request.url:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="URL target cannot be empty"
        )
    
    # Feature extraction
    features_info = extract_url_features(request.url)
    vector = features_info["features_vector"]
    
    # ML Prediction
    score, verdict = model_manager.predict_threat("url", vector)
    
    # Database Logging
    log_scan(
        scan_type="URL",
        target=request.url,
        score=score,
        result=verdict,
        active_model=model_manager.active_model_name,
        metadata={
            "is_https": features_info["is_https"],
            "is_ip_host": features_info["is_ip_host"],
            "dot_count": features_info["dot_count"],
            "slash_count": features_info["slash_count"],
            "dash_count": features_info["dash_count"],
            "sensitive_word_matches": features_info["sensitive_word_matches"]
        }
    )
    
    return {
        "type": "URL",
        "target": request.url,
        "score": score,
        "result": verdict,
        "active_model": model_manager.active_model_name,
        "metadata": {
            "is_https": features_info["is_https"],
            "is_ip_host": features_info["is_ip_host"],
            "dot_count": features_info["dot_count"],
            "slash_count": features_info["slash_count"],
            "dash_count": features_info["dash_count"],
            "sensitive_word_matches": features_info["sensitive_word_matches"]
        }
    }

@router.post("/apk")
def scan_apk(file: UploadFile = File(...)):
    if not file.filename.endswith(('.apk', '.zip')):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Unsupported package binary type"
        )
    
    # Create temp directory
    temp_dir = "temp_scans"
    os.makedirs(temp_dir, exist_ok=True)
    temp_file_path = os.path.join(temp_dir, file.filename)
    
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        # Feature extraction
        apk_info = extract_apk_features(temp_file_path)
        vector = apk_info["features_vector"]
        
        # Prediction
        score, verdict = model_manager.predict_threat("apk", vector)
        
        # Log to Database
        log_scan(
            scan_type="APK",
            target=file.filename,
            score=score,
            result=verdict,
            active_model=model_manager.active_model_name,
            metadata={
                "permissions_count": apk_info["permissions_count"],
                "permissions_list": apk_info["permissions_list"],
                "dangerous_permissions_found": apk_info["dangerous_permissions_found"],
                "target_sdk": apk_info["target_sdk"],
                "activities_count": apk_info["activities_count"],
                "services_count": apk_info["services_count"],
                "receivers_count": apk_info["receivers_count"]
            }
        )
        
        return {
            "type": "APK",
            "target": file.filename,
            "score": score,
            "result": verdict,
            "active_model": model_manager.active_model_name,
            "metadata": {
                "permissions_count": apk_info["permissions_count"],
                "permissions_list": apk_info["permissions_list"],
                "dangerous_permissions_found": apk_info["dangerous_permissions_found"],
                "target_sdk": apk_info["target_sdk"],
                "activities_count": apk_info["activities_count"],
                "services_count": apk_info["services_count"],
                "receivers_count": apk_info["receivers_count"]
            }
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Decompiling / parsing error occurred: {str(e)}"
        )
    finally:
        # Cleanup
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
