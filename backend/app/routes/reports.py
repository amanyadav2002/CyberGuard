from fastapi import APIRouter
from app.database import get_scans_history, clear_scans_history, delete_scan

router = APIRouter(prefix="/api/reports", tags=["reports"])

@router.get("/dashboard")
def get_dashboard_reports():
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
def clear_reports():
    clear_scans_history()
    return {"message": "Datalog records purged successfully"}

@router.delete("/scan/{scan_id}")
def delete_single_scan(scan_id: str):
    delete_scan(scan_id)
    return {"message": "Scan record deleted successfully"}

@router.delete("/{scan_id}")
def delete_report_by_id(scan_id: str):
    delete_scan(scan_id)
    return {"message": "Scan record deleted successfully"}
