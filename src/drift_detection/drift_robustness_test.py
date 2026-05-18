import pandas as pd
import joblib

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score
)

from xgboost import XGBClassifier

from src.features.build_features import (
    create_binary_target
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
    r"\drift_robust_xgboost.pkl"
)


# =====================================
# Load Dataset
# =====================================

print("\nLoading drift dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset loaded")


# =====================================
# Feature Engineering
# =====================================

df = create_binary_target(df)

print("Binary target created")


# =====================================
# Train/Test Temporal Split
# =====================================

train_df = df[
    df['Day'].isin([
        'Monday',
        'Tuesday'
    ])
]

test_df = df[
    df['Day'] == 'Friday'
]

print("\nTrain Shape:")
print(train_df.shape)

print("\nTest Shape:")
print(test_df.shape)


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
# Train Model
# =====================================

print("\nTraining XGBoost model...")

model = XGBClassifier(

    random_state=42,

    eval_metric='logloss',

    use_label_encoder=False
)

model.fit(
    X_train,
    y_train
)

print("Model trained")


# =====================================
# Predictions
# =====================================

print("\nGenerating predictions...")

y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

print("Predictions generated")


# =====================================
# Evaluation
# =====================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

roc_auc = roc_auc_score(
    y_test,
    y_prob
)

print("\n==============================")
print("DRIFT ROBUSTNESS RESULTS")
print("==============================")

print(f"\nAccuracy: {accuracy}")

print(f"\nROC-AUC: {roc_auc}")

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred
    )
)

print("\nConfusion Matrix:\n")

print(
    confusion_matrix(
        y_test,
        y_pred
    )
)


# =====================================
# Save Model
# =====================================

joblib.dump(
    model,
    MODEL_SAVE_PATH
)

print(
    f"\nModel saved at:\n"
    f"{MODEL_SAVE_PATH}"
)