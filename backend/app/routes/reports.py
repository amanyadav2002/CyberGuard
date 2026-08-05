from fastapi import APIRouter, Depends
from app.database import get_scans_history, clear_scans_history
from app.auth import get_current_user_username

router = APIRouter(prefix="/api/reports", tags=["reports"])

@router.get("/dashboard")
def get_dashboard_reports(username: str = Depends(get_current_user_username)):
    scans = get_scans_history()
    total = len(scans)
    malicious = sum(1 for s in scans if s["result"] == "Malicious" or s["score"] >= 50.0)
    safe = total - malicious
    
    ratio = float(round((malicious / total) * 100, 1)) if total > 0 else 0.0
    
    return {
        "total_scans": total,
        "malicious_scans": malicious,
        "safe_scans": safe,
        "threat_ratio": ratio,
        "scans": scans
    }

@router.delete("/clear")
def clear_reports(username: str = Depends(get_current_user_username)):
    clear_scans_history()
    return {"message": "Datalog records purged successfully"}
