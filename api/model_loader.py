import joblib


MODEL_PATH = (
    r"models"
    r"\enhanced_drift_xgboost.pkl"
)


model = joblib.load(
    MODEL_PATH
)