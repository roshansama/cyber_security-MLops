import joblib


MODEL_PATH = (
    r"D:\MLOPS\models"
    r"\enhanced_drift_xgboost.pkl"
)


model = joblib.load(
    MODEL_PATH
)