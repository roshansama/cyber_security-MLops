import pandas as pd
import mlflow
import mlflow.xgboost
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.metrics import (

    accuracy_score,

    precision_score,

    recall_score,

    f1_score,

    roc_auc_score,

    confusion_matrix
)

from xgboost import XGBClassifier

from src.features.build_features import (
    create_binary_target
)


# =====================================
# MLflow Config
# =====================================

mlflow.set_experiment(
    "Drift Robust IDS"
)


# =====================================
# Paths
# =====================================

DATA_PATH = (
    r"D:\MLOPS\data\processed"
    r"\drift_dataset.csv"
)

MODEL_SAVE_PATH = (
    r"D:\MLOPS\models"
    r"\mlflow_xgboost.pkl"
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
# Temporal Split
# =====================================

train_df = df[
    df['Day'].isin([
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday'
    ])
]

test_df = df[
    df['Day'] == 'Friday'
]


# =====================================
# Features & Target
# =====================================

drop_columns = [
    'Label',
    'Binary_Label',
    'Day'
]

X_train = train_df.drop(
    columns=drop_columns
)

y_train = train_df['Binary_Label']

X_test = test_df.drop(
    columns=drop_columns
)

y_test = test_df['Binary_Label']


# =====================================
# MLflow Run
# =====================================

with mlflow.start_run():

    print("\nTraining model...")

    threshold = 0.30

    model = XGBClassifier(

        random_state=42,

        eval_metric='logloss'
    )

    model.fit(
        X_train,
        y_train
    )

    print("Model trained")


    # =================================
    # Predictions
    # =================================

    y_prob = model.predict_proba(
        X_test
    )[:, 1]

    y_pred = (
        y_prob >= threshold
    ).astype(int)


    # =================================
    # Metrics
    # =================================

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


    # =================================
    # Log Parameters
    # =================================

    mlflow.log_param(
        "model",
        "XGBoost"
    )

    mlflow.log_param(
        "threshold",
        threshold
    )

    mlflow.log_param(
        "temporal_training",
        "Mon-Thu"
    )

    mlflow.log_param(
        "test_day",
        "Friday"
    )


    # =================================
    # Log Metrics
    # =================================

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


    # =================================
    # Confusion Matrix
    # =================================

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    plt.figure(figsize=(6, 5))

    sns.heatmap(
        cm,
        annot=True,
        fmt='d'
    )

    plt.title(
        "Confusion Matrix"
    )

    plt.xlabel(
        "Predicted"
    )

    plt.ylabel(
        "Actual"
    )

    confusion_matrix_path = (
        "confusion_matrix.png"
    )

    plt.savefig(
        confusion_matrix_path
    )

    plt.close()


    # =================================
    # Log Artifacts
    # =================================

    mlflow.log_artifact(
        confusion_matrix_path
    )


    # =================================
    # Log Model
    # =================================

    mlflow.xgboost.log_model(
        model,
        artifact_path="model"
    )


    # =================================
    # Save Local Model
    # =================================

    joblib.dump(
        model,
        MODEL_SAVE_PATH
    )


    # =================================
    # Console Output
    # =================================

    print("\n======================")
    print("MLFLOW RESULTS")
    print("======================")

    print(f"\nAccuracy: {accuracy}")

    print(f"\nPrecision: {precision}")

    print(f"\nRecall: {recall}")

    print(f"\nF1 Score: {f1}")

    print(f"\nROC-AUC: {roc_auc}")

    print(
        "\nRun successfully logged "
        "to MLflow"
    )