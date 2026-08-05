import os
import sqlite3
import json
from datetime import datetime
from pymongo import MongoClient

DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "security_platform.db")

# MongoDB settings
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
mongo_client = None
mongo_db = None
use_mongodb = False

# Try checking if MongoDB is active
try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=1000)
    client.server_info()  # Forces a call to see if connected
    mongo_client = client
    mongo_db = mongo_client["cyberguard"]
    use_mongodb = True
    print("Database bound: Connected to MONGODB.")
except Exception:
    print("Database bound: MongoDB offline. Falling back to SQLITE.")

def get_sqlite_conn():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if use_mongodb:
        # MongoDB does not require schema initialization
        return
    
    conn = get_sqlite_conn()
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)
    
    # Create scans table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            target TEXT NOT NULL,
            score REAL NOT NULL,
            result TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            active_model TEXT NOT NULL,
            metadata TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

# Users Operations
def get_user(username: str):
    if use_mongodb:
        user = mongo_db["users"].find_one({"username": username})
        if user:
            user["id"] = str(user["_id"])
        return user
    
    conn = get_sqlite_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def create_user(username: str, email: str, password_hash: str):
    if use_mongodb:
        mongo_db["users"].insert_one({
            "username": username,
            "email": email,
            "password_hash": password_hash
        })
        return True
    
    conn = get_sqlite_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            (username, email, password_hash)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Scans History Operations
def log_scan(scan_type: str, target: str, score: float, result: str, active_model: str, metadata: dict):
    timestamp = datetime.utcnow().isoformat()
    if use_mongodb:
        mongo_db["scans"].insert_one({
            "type": scan_type,
            "target": target,
            "score": score,
            "result": result,
            "timestamp": timestamp,
            "active_model": active_model,
            "metadata": metadata
        })
        return
    
    conn = get_sqlite_conn()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO scans (type, target, score, result, timestamp, active_model, metadata) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (scan_type, target, score, result, timestamp, active_model, json.dumps(metadata))
    )
    conn.commit()
    conn.close()

def get_scans_history():
    if use_mongodb:
        scans = list(mongo_db["scans"].find().sort("timestamp", -1).limit(50))
        for scan in scans:
            scan["id"] = str(scan["_id"])
            del scan["_id"]
        return scans
    
    conn = get_sqlite_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM scans ORDER BY timestamp DESC LIMIT 50")
    rows = cursor.fetchall()
    conn.close()
    
    results = []
    for r in rows:
        item = dict(r)
        # Parse SQLite metadata string back to dict
        try:
            item["metadata"] = json.loads(item["metadata"])
        except Exception:
            item["metadata"] = {}
        results.append(item)
    return results

def clear_scans_history():
    if use_mongodb:
        mongo_db["scans"].delete_many({})
        return
    
    conn = get_sqlite_conn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM scans")
    conn.commit()
    conn.close()
