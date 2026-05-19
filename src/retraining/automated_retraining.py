import os
import joblib
import mlflow
import warnings

import pandas as pd

from xgboost import XGBClassifier

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

warnings.filterwarnings(
    "ignore"
)


# =====================================
# CONFIG
# =====================================

DRIFT_THRESHOLD = 0.25

MODEL_SAVE_PATH = (
    "models"
)

CURRENT_MODEL_PATH = (
    "models/enhanced_drift_xgboost.pkl"
)

DRIFT_RESULTS_PATH = (
    "data/processed/psi_drift_results.csv"
)

DATASET_PATH = (
    "data/processed/drift_dataset.csv"
)


# =====================================
# LOAD DRIFT RESULTS
# =====================================

print("\nLoading drift results...")

drift_df = pd.read_csv(
    DRIFT_RESULTS_PATH
)

print("Drift results loaded")


# =====================================
# CHECK RETRAINING CONDITION
# =====================================

max_psi = drift_df[
    "PSI Score"
].max()

print(
    "\nMaximum PSI:",
    max_psi
)


if max_psi < DRIFT_THRESHOLD:

    print(
        "\nNo retraining required"
    )

    exit()


print(
    "\nSignificant drift detected"
)

print(
    "Starting retraining pipeline..."
)


# =====================================
# LOAD DATASET
# =====================================

print("\nLoading dataset...")

df = pd.read_csv(
    DATASET_PATH
)

print("Dataset loaded")

# =====================================
# REMOVE NON-NUMERIC COLUMNS
# =====================================

object_columns = df.select_dtypes(
    include=["object"]
).columns.tolist()

print(
    "\nObject Columns Found:"
)

print(
    object_columns
)


# Keep Label for target creation
object_columns.remove(
    "Label"
)

print(
    "\nDropping Object Columns:"
)

print(
    object_columns
)


df = df.drop(
    columns=object_columns
)


# =====================================
# TARGET CREATION
# =====================================

df["Target"] = df[
    "Label"
].apply(

    lambda x:
    0 if x == "BENIGN"
    else 1
)


# =====================================
# FEATURES / TARGET
# =====================================

X = df.drop(
    columns=[
        "Label",
        "Target"
    ]
)

y = df[
    "Target"
]


# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)


print("\nTrain Shape:")
print(X_train.shape)

print("\nTest Shape:")
print(X_test.shape)


# =====================================
# MLFLOW TRACKING
# =====================================

mlflow.set_experiment(
    "Automated Retraining IDS"
)


with mlflow.start_run():

    # ================================
    # MODEL
    # ================================

    print("\nTraining model...")


    model = XGBClassifier(

        n_estimators=200,

        max_depth=8,

        learning_rate=0.1,

        subsample=0.8,

        colsample_bytree=0.8,

        eval_metric="logloss",

        random_state=42
    )


    model.fit(
        X_train,
        y_train
    )

    print("Model trained")


    # ================================
    # PREDICTIONS
    # ================================

    y_pred = model.predict(
        X_test
    )

    y_proba = model.predict_proba(
        X_test
    )[:, 1]


    # ================================
    # METRICS
    # ================================

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
        y_proba
    )


    # ================================
    # LOG MLFLOW
    # ================================

    mlflow.log_param(
        "trigger_reason",
        "PSI Drift"
    )

    mlflow.log_param(
        "max_psi",
        max_psi
    )


    mlflow.log_metric(
        "accuracy",
        accuracy
    )

    mlflow.log_metric(
        "precision",
        precision
    )

    mlflow.log_metric(
        "recall",
        recall
    )

    mlflow.log_metric(
        "f1_score",
        f1
    )

    mlflow.log_metric(
        "roc_auc",
        roc_auc
    )


    # ================================
    # SAVE NEW MODEL
    # ================================

    new_model_path = os.path.join(

        MODEL_SAVE_PATH,

        "auto_retrained_xgboost.pkl"
    )


    joblib.dump(
        model,
        new_model_path
    )


    mlflow.log_artifact(
        new_model_path
    )


    # ================================
    # FINAL REPORT
    # ================================

    print("\n==============================")
    print("AUTOMATED RETRAINING COMPLETE")
    print("==============================")


    print("\nAccuracy:", accuracy)

    print("\nPrecision:", precision)

    print("\nRecall:", recall)

    print("\nF1 Score:", f1)

    print("\nROC-AUC:", roc_auc)


    print("\nNew Model Saved At:")
    print(new_model_path)


    print("\nMLflow Run Logged")