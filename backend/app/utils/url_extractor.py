import re
from urllib.parse import urlparse

SENSITIVE_WORDS = ['login', 'secure', 'verify', 'update', 'banking', 'signin', 'account', 'paypal', 'ebay', 'amazon', 'webscr']

def extract_url_features(url: str) -> dict:
    url_lower = url.lower()
    
    # SSL check
    is_https = 1 if url_lower.startswith("https://") else 0
    
    # Parse host
    try:
        if "://" in url_lower:
            parsed = urlparse(url)
            host = parsed.hostname or parsed.path.split('/')[0]
        else:
            host = url_lower.split('/')[0]
    except Exception:
        host = url_lower
        
    # IP Host check
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    is_ip_host = 1 if re.match(ip_pattern, host) else 0
    
    # Counts
    dot_count = url_lower.count('.')
    slash_count = url_lower.count('/')
    dash_count = url_lower.count('-')
    
    # Sensitive words match
    sensitive_word_count = sum(1 for word in SENSITIVE_WORDS if word in url_lower)
    matched_words = [word for word in SENSITIVE_WORDS if word in url_lower]

    return {
        "features_vector": [is_https, is_ip_host, dot_count, slash_count, dash_count, sensitive_word_count],
        "is_https": bool(is_https),
        "is_ip_host": bool(is_ip_host),
        "dot_count": dot_count,
        "slash_count": slash_count,
        "dash_count": dash_count,
        "sensitive_word_matches": matched_words
    }
