import pandas as pd
import joblib

from sklearn.metrics import (

    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    precision_score,
    recall_score,
    f1_score
)

from xgboost import XGBClassifier

from src.features.build_features import (
    create_binary_target
)

# =====================================
# FILE PATHS
# =====================================

DATA_PATH = (
    "data/processed/drift_dataset.csv"
)

MODEL_SAVE_PATH = (
    "models/drift_robust_xgboost.pkl"
)

# =====================================
# LOAD DATASET
# =====================================

print("\nLoading drift dataset...")

df = pd.read_csv(
    DATA_PATH
)

print("Drift dataset loaded successfully")

# =====================================
# FEATURE ENGINEERING
# =====================================

print("\nCreating binary target...")

df = create_binary_target(df)

print("Binary target created successfully")

# =====================================
# TEMPORAL TRAIN / TEST SPLIT
# =====================================

print("\nCreating temporal train-test split...")

train_df = df[
    df["Day"].isin([
        "Monday",
        "Tuesday"
    ])
]

test_df = df[
    df["Day"] == "Friday"
]

print(f"\nTrain Dataset Shape: {train_df.shape}")

print(f"\nTest Dataset Shape: {test_df.shape}")

# =====================================
# FEATURES & TARGET
# =====================================

drop_columns = [

    "Label",
    "Binary_Label",
    "Day"
]

print("\nPreparing feature matrices...")

X_train = train_df.drop(
    columns=drop_columns
)

y_train = train_df["Binary_Label"]

X_test = test_df.drop(
    columns=drop_columns
)

y_test = test_df["Binary_Label"]

print("Feature matrices prepared successfully")

# =====================================
# TRAIN MODEL
# =====================================

print("\nTraining XGBoost drift-robust model...")

model = XGBClassifier(

    random_state=42,

    eval_metric="logloss",

    use_label_encoder=False,

    n_estimators=200,

    max_depth=8,

    learning_rate=0.1,

    subsample=0.8,

    colsample_bytree=0.8,

    n_jobs=-1
)

model.fit(

    X_train,

    y_train
)

print("XGBoost model trained successfully")

# =====================================
# GENERATE PREDICTIONS
# =====================================

print("\nGenerating predictions...")

y_pred = model.predict(
    X_test
)

y_prob = model.predict_proba(
    X_test
)[:, 1]

print("Predictions generated successfully")

# =====================================
# EVALUATION METRICS
# =====================================

print("\nCalculating evaluation metrics...")

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

# =====================================
# DISPLAY RESULTS
# =====================================

print("\n=====================================")
print("DRIFT ROBUSTNESS EVALUATION RESULTS")
print("=====================================")

print(f"\nAccuracy  : {round(accuracy, 6)}")

print(f"\nPrecision : {round(precision, 6)}")

print(f"\nRecall    : {round(recall, 6)}")

print(f"\nF1 Score  : {round(f1, 6)}")

print(f"\nROC-AUC   : {round(roc_auc, 6)}")

# =====================================
# CLASSIFICATION REPORT
# =====================================

print("\n=====================================")
print("CLASSIFICATION REPORT")
print("=====================================\n")

print(

    classification_report(

        y_test,

        y_pred
    )
)

# =====================================
# CONFUSION MATRIX
# =====================================

print("\n=====================================")
print("CONFUSION MATRIX")
print("=====================================\n")

print(

    confusion_matrix(

        y_test,

        y_pred
    )
)

# =====================================
# SAVE MODEL
# =====================================

print("\nSaving drift-robust XGBoost model...")

joblib.dump(

    model,

    MODEL_SAVE_PATH
)

print("Model saved successfully")

print(f"\nModel Path:\n{MODEL_SAVE_PATH}")

# =====================================
# FINAL SUMMARY
# =====================================

print("\n=====================================")
print("DRIFT ROBUSTNESS PIPELINE COMPLETE")
print("=====================================")

print("\nPipeline Achievements:")

print("- Temporal drift validation completed")

print("- Cross-day robustness evaluated")

print("- Production-grade XGBoost model trained")

print("- Model artifact exported successfully")

print("- Drift resilience benchmark completed")