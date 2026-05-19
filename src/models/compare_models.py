import os
import time
import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from src.features.build_features import (
    create_binary_target
)

from src.models.train_model import (
    split_data
)

from src.models.model_factory import (
    get_models
)


# =========================
# Paths
# =========================

DATA_PATH = (
    "data/processed/cleaned_cicids2017.csv"
)

RESULTS_PATH = (
    "data/processed/model_comparison_results.csv"
)

MODEL_SAVE_DIR = "models"


# Create models directory if missing
os.makedirs(
    MODEL_SAVE_DIR,
    exist_ok=True
)


# =========================
# Load Dataset
# =========================

print("\nLoading dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded")


# =========================
# Feature Engineering
# =========================

print("\nCreating binary target...")

df = create_binary_target(df)

print("Binary target created")


# =========================
# Train-Test Split
# =========================

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = split_data(df)

print("Dataset split completed")


# =========================
# Load Models
# =========================

models = get_models()


# =========================
# Benchmark Models
# =========================

results = []

best_model = None

best_model_name = ""

best_roc_auc = 0


for model_name, model in models.items():

    print(f"\nTraining {model_name}...")

    start_time = time.time()

    # Train model
    model.fit(X_train, y_train)

    end_time = time.time()

    training_time = end_time - start_time

    # Predictions
    y_pred = model.predict(X_test)

    # Probabilities
    y_prob = model.predict_proba(X_test)[:, 1]

    # Metrics
    accuracy = accuracy_score(
        y_test,
        y_pred
    )

    precision = precision_score(
        y_test,
        y_pred
    )

    recall = recall_score(
        y_test,
        y_pred
    )

    f1 = f1_score(
        y_test,
        y_pred
    )

    roc_auc = roc_auc_score(
        y_test,
        y_prob
    )

    # Store results
    results.append({
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC AUC": roc_auc,
        "Training Time (s)": training_time
    })

    print(f"{model_name} completed")

    print(f"ROC-AUC: {roc_auc}")

    # Track best model
    if roc_auc > best_roc_auc:

        best_roc_auc = roc_auc

        best_model = model

        best_model_name = model_name


# =========================
# Save Results
# =========================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by="ROC AUC",
    ascending=False
)

results_df.to_csv(
    RESULTS_PATH,
    index=False
)

print("\nModel comparison results saved")


# =========================
# Save Best Model
# =========================

best_model_path = (
    f"{MODEL_SAVE_DIR}"
    f"/best_model.pkl"
)

joblib.dump(
    best_model,
    best_model_path
)

print(
    f"\nBest model saved: "
    f"{best_model_name}"
)

print(
    f"Best ROC-AUC: "
    f"{best_roc_auc}"
)

print(
    f"Model saved at:\n"
    f"{best_model_path}"
)


# =========================
# Display Results
# =========================

print("\nFinal Benchmark Results:\n")

print(results_df)