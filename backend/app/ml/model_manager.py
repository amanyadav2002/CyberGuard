import os
import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier

from app.utils.dataset_generator import generate_url_dataset, generate_apk_dataset

MODEL_DIR = os.path.join(os.path.dirname(__file__), "saved_models")
os.makedirs(MODEL_DIR, exist_ok=True)

MODEL_NAMES_MAP = {
    "Logistic Regression": "Logistic_Regression",
    "Decision Tree": "Decision_Tree",
    "Random Forest": "Random_Forest",
    "SVM": "SVM",
    "MLP": "MLP",
    "XGBoost": "XGBoost"
}

class ModelManager:
    def __init__(self):
        self.active_model_name = "Random Forest"
        self.models_cache = {}
        
    def get_model_path(self, task: str, model_name: str) -> str:
        file_friendly_name = MODEL_NAMES_MAP.get(model_name, model_name.replace(" ", "_"))
        return os.path.join(MODEL_DIR, f"{task}_{file_friendly_name}.pkl")

    def initialize_all_models(self, force_retrain: bool = False):
        print("ModelManager: Initializing models...")
        
        # Check if we need to train
        needs_training = False
        for task in ["url", "apk"]:
            for name in MODEL_NAMES_MAP.keys():
                path = self.get_model_path(task, name)
                if not os.path.exists(path):
                    needs_training = True
                    break
        
        if needs_training or force_retrain:
            print("ModelManager: PKL models missing. Running statistical training pipeline...")
            self.train_and_save_all_models()
        else:
            print("ModelManager: Cached models found. Loading models to memory...")
            self.load_models_to_cache()

    def train_and_save_all_models(self):
        # 1. URL training
        print("ModelManager: Synthesizing URL datasets...")
        url_df = generate_url_dataset(1500)
        X_url = url_df.drop("label", axis=1)
        y_url = url_df["label"]

        # 2. APK training
        print("ModelManager: Synthesizing APK datasets...")
        apk_df = generate_apk_dataset(1500)
        X_apk = apk_df.drop("label", axis=1)
        y_apk = apk_df["label"]

        # Define classifiers
        classifiers = {
            "Logistic Regression": LogisticRegression(),
            "Decision Tree": DecisionTreeClassifier(max_depth=6),
            "Random Forest": RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42),
            "SVM": SVC(probability=True, kernel="rbf", C=1.0),
            "MLP": MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500, random_state=42),
            "XGBoost": XGBClassifier(max_depth=4, eval_metric="logloss")
        }

        # Train and save
        for name, clf in classifiers.items():
            # URL model
            print(f"ModelManager: Training URL -> {name}")
            clf.fit(X_url, y_url)
            joblib.dump(clf, self.get_model_path("url", name))
            
            # Recreate model to avoid fitting conflicts
            if name == "XGBoost":
                clf_apk = XGBClassifier(max_depth=4, eval_metric="logloss")
            elif name == "SVM":
                clf_apk = SVC(probability=True, kernel="rbf", C=1.0)
            elif name == "MLP":
                clf_apk = MLPClassifier(hidden_layer_sizes=(16, 8), max_iter=500, random_state=42)
            else:
                from copy import deepcopy
                clf_apk = deepcopy(clf)
                
            # APK model
            print(f"ModelManager: Training APK -> {name}")
            clf_apk.fit(X_apk, y_apk)
            joblib.dump(clf_apk, self.get_model_path("apk", name))

        print("ModelManager: Training complete. Models serialized.")
        self.load_models_to_cache()

    def load_models_to_cache(self):
        for task in ["url", "apk"]:
            self.models_cache[task] = {}
            for name in MODEL_NAMES_MAP.keys():
                path = self.get_model_path(task, name)
                if os.path.exists(path):
                    self.models_cache[task][name] = joblib.load(path)
                else:
                    raise FileNotFoundError(f"Model file not found at {path}. Rerun initialization.")

    def set_active_model(self, name: str):
        if name in MODEL_NAMES_MAP:
            self.active_model_name = name
            return True
        return False

    def predict_threat(self, task: str, features: list) -> tuple:
        model = self.models_cache.get(task, {}).get(self.active_model_name)
        if model is None:
            # Fallback if cache missed
            return 50.0, "Suspicious"
            
        features_arr = np.array(features).reshape(1, -1)
        
        # Predict probability
        prob = model.predict_proba(features_arr)[0][1] # Probability of class 1 (Malicious)
        score_percent = float(round(prob * 100, 1))
        
        verdict = "Malicious" if score_percent >= 50.0 else "Safe"
        return score_percent, verdict

# Global model manager singleton
model_manager = ModelManager()
