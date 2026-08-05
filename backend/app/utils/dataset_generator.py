import numpy as np
import pandas as pd

def generate_url_dataset(num_samples: int = 1500) -> pd.DataFrame:
    np.random.seed(42)
    half_samples = num_samples // 2
    
    # SAFE URL samples (label = 0)
    safe_https = np.random.binomial(1, 0.95, half_samples)
    safe_ip = np.random.binomial(1, 0.01, half_samples)
    safe_dots = np.random.poisson(1.8, half_samples)
    safe_slashes = np.random.poisson(2.1, half_samples)
    safe_dashes = np.random.poisson(0.3, half_samples)
    safe_keywords = np.random.binomial(2, 0.05, half_samples)
    safe_labels = np.zeros(half_samples, dtype=int)
    
    # PHISHING URL samples (label = 1)
    phish_https = np.random.binomial(1, 0.10, half_samples)
    phish_ip = np.random.binomial(1, 0.35, half_samples)
    phish_dots = np.random.poisson(3.8, half_samples)
    phish_slashes = np.random.poisson(4.5, half_samples)
    phish_dashes = np.random.poisson(1.9, half_samples)
    phish_keywords = np.random.binomial(3, 0.65, half_samples) + 1  # at least one
    phish_labels = np.ones(half_samples, dtype=int)
    
    # Combine
    data = {
        "is_https": np.concatenate([safe_https, phish_https]),
        "is_ip_host": np.concatenate([safe_ip, phish_ip]),
        "dot_count": np.concatenate([safe_dots, phish_dots]),
        "slash_count": np.concatenate([safe_slashes, phish_slashes]),
        "dash_count": np.concatenate([safe_dashes, phish_dashes]),
        "sensitive_word_count": np.concatenate([safe_keywords, phish_keywords]),
        "label": np.concatenate([safe_labels, phish_labels])
    }
    
    df = pd.DataFrame(data)
    # Shuffle
    return df.sample(frac=1.0).reset_index(drop=True)

def generate_apk_dataset(num_samples: int = 1500) -> pd.DataFrame:
    np.random.seed(24)
    half_samples = num_samples // 2
    
    # SAFE APK samples (label = 0)
    safe_perms = np.random.poisson(5.2, half_samples) + 1
    safe_boot = np.random.binomial(1, 0.05, half_samples)
    safe_sms = np.random.binomial(1, 0.02, half_samples)
    safe_activities = np.random.poisson(12.5, half_samples) + 2
    safe_services = np.random.poisson(2.1, half_samples) + 1
    safe_labels = np.zeros(half_samples, dtype=int)
    
    # MALICIOUS APK samples (label = 1)
    mal_perms = np.random.poisson(22.4, half_samples) + 5
    mal_boot = np.random.binomial(1, 0.85, half_samples)
    mal_sms = np.random.binomial(1, 0.75, half_samples)
    mal_activities = np.random.poisson(3.8, half_samples) + 1
    mal_services = np.random.poisson(6.2, half_samples) + 2
    mal_labels = np.ones(half_samples, dtype=int)
    
    # Combine
    data = {
        "permissions_count": np.concatenate([safe_perms, mal_perms]),
        "has_boot_permission": np.concatenate([safe_boot, mal_boot]),
        "has_sms_permission": np.concatenate([safe_sms, mal_sms]),
        "activities_count": np.concatenate([safe_activities, mal_activities]),
        "services_count": np.concatenate([safe_services, mal_services]),
        "label": np.concatenate([safe_labels, mal_labels])
    }
    
    df = pd.DataFrame(data)
    # Shuffle
    return df.sample(frac=1.0).reset_index(drop=True)
