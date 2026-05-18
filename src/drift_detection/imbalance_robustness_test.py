import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.metrics import (

    accuracy_score,

    classification_report,

    confusion_matrix,

    roc_auc_score,

    precision_recall_curve
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
    r"\imbalance_robust_xgboost.pkl"
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
# Calculate Class Imbalance
# =====================================

negative_count = (
    y_train == 0
).sum()

positive_count = (
    y_train == 1
).sum()

scale_pos_weight = (
    negative_count / positive_count
)

print(
    f"\nScale Pos Weight: "
    f"{scale_pos_weight}"
)


# =====================================
# Train Model
# =====================================

print("\nTraining imbalance-aware model...")

model = XGBClassifier(

    random_state=42,

    eval_metric='logloss',

    scale_pos_weight=scale_pos_weight
)

model.fit(
    X_train,
    y_train
)

print("Model trained")


# =====================================
# Predictions
# =====================================

y_prob = model.predict_proba(X_test)[:, 1]

threshold = 0.30

print(f"\nUsing Threshold: {threshold}")

y_pred = (
    y_prob >= threshold
).astype(int)


# =====================================
# Metrics
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
print("IMBALANCE ROBUSTNESS RESULTS")
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
# Precision Recall Curve
# =====================================

precision, recall, thresholds = (
    precision_recall_curve(
        y_test,
        y_prob
    )
)

plt.figure(figsize=(8, 6))

plt.plot(
    recall,
    precision
)

plt.xlabel("Recall")

plt.ylabel("Precision")

plt.title(
    "Imbalance-Aware Precision-Recall Curve"
)

plt.grid(True)

plt.show()


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