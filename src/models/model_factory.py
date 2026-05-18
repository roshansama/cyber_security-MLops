from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier
)

from xgboost import XGBClassifier

from lightgbm import LGBMClassifier

from catboost import CatBoostClassifier


def get_models():

    models = {

        "RandomForest":
        RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        ),

        "AdaBoost":
        AdaBoostClassifier(
            n_estimators=100,
            random_state=42
        ),

        "GradientBoosting":
        GradientBoostingClassifier(
            n_estimators=100,
            random_state=42
        ),

        "XGBoost":
        XGBClassifier(
            n_estimators=100,
            random_state=42,
            eval_metric='logloss',
            use_label_encoder=False
        ),

        "LightGBM":
        LGBMClassifier(
            n_estimators=100,
            random_state=42
        ),

        "CatBoost":
        CatBoostClassifier(
            iterations=100,
            random_state=42,
            verbose=0
        )
    }

    return models