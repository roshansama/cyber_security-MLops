import os
import time
import joblib
import pandas as pd

from sklearn.model_selection import (
    train_test_split,
    RandomizedSearchCV
)

from sklearn.metrics import (
    roc_auc_score
)

from xgboost import XGBClassifier

from lightgbm import LGBMClassifier

from src.features.build_features import (
    create_binary_target
)

from src.models.hyperparameter_config import (
    PARAM_GRID
)


# =====================================
# Paths
# =====================================

DATA_PATH = (
    r"D:\MLOPS\data\processed"
    r"\cleaned_cicids2017.csv"
)

MODEL_DIR = (
    r"D:\MLOPS\models"
)

RESULTS_PATH = (
    r"D:\MLOPS\data\processed"
    r"\tuning_results.csv"
)


# Create model directory
os.makedirs(
    MODEL_DIR,
    exist_ok=True
)


# =====================================
# Load Dataset
# =====================================

print("\nLoading dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset loaded")


# =====================================
# Feature Engineering
# =====================================

df = create_binary_target(df)

print("Binary target created")


# =====================================
# Sample Dataset
# =====================================

print("\nSampling dataset...")

df = df.sample(
    n=300000,
    random_state=42
)

print("Dataset sampled")


# =====================================
# Split Dataset
# =====================================

X = df.drop(
    columns=['Label', 'Binary_Label']
)

y = df['Binary_Label']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Train-test split completed")


# =====================================
# Models To Tune
# =====================================

models = {

    "XGBoost":
    XGBClassifier(
        random_state=42,
        eval_metric='logloss',
        use_label_encoder=False
    ),

    "LightGBM":
    LGBMClassifier(
        random_state=42
    )
}


# =====================================
# Store Results
# =====================================

results = []


# =====================================
# Tune Models
# =====================================

for model_name, model in models.items():

    print(f"\nTuning {model_name}...")

    param_grid = PARAM_GRID[model_name]

    random_search = RandomizedSearchCV(

        estimator=model,

        param_distributions=param_grid,

        n_iter=10,

        scoring='roc_auc',

        cv=3,

        verbose=2,

        random_state=42,

        n_jobs=-1
    )

    start_time = time.time()

    random_search.fit(
        X_train,
        y_train
    )

    end_time = time.time()

    training_time = end_time - start_time

    # Best model
    best_model = random_search.best_estimator_

    # Predictions
    y_prob = best_model.predict_proba(X_test)[:, 1]

    roc_auc = roc_auc_score(
        y_test,
        y_prob
    )

    # Save model
    model_path = (
        f"{MODEL_DIR}"
        f"\\best_{model_name}.pkl"
    )

    joblib.dump(
        best_model,
        model_path
    )

    # Save results
    results.append({

        "Model": model_name,

        "Best ROC AUC": roc_auc,

        "Best Parameters":
        random_search.best_params_,

        "Training Time (s)":
        training_time,

        "Saved Model Path":
        model_path
    })

    print(f"\n{model_name} tuning completed")

    print(f"Best ROC-AUC: {roc_auc}")

    print(f"Model saved at:\n{model_path}")


# =====================================
# Save Results
# =====================================

results_df = pd.DataFrame(results)

results_df.to_csv(
    RESULTS_PATH,
    index=False
)

print("\nTuning results saved")

print("\nFinal Tuning Results:\n")

print(results_df)