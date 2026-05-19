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
# FILE PATHS
# =====================================

DATA_PATH = (
    "data/processed/cleaned_cicids2017.csv"
)

MODEL_DIR = (
    "models"
)

RESULTS_PATH = (
    "data/processed/tuning_results.csv"
)

# =====================================
# CREATE MODEL DIRECTORY
# =====================================

os.makedirs(

    MODEL_DIR,

    exist_ok=True
)

print("\nModel directory verified")

# =====================================
# LOAD DATASET
# =====================================

print("\nLoading processed dataset...")

df = pd.read_csv(
    DATA_PATH
)

print("Dataset loaded successfully")

print(f"\nDataset Shape: {df.shape}")

# =====================================
# FEATURE ENGINEERING
# =====================================

print("\nCreating binary target...")

df = create_binary_target(
    df
)

print("Binary target created successfully")

# =====================================
# SAMPLE DATASET
# =====================================

print("\nSampling dataset for tuning...")

df = df.sample(

    n=300000,

    random_state=42
)

print("Dataset sampled successfully")

print(f"\nSampled Dataset Shape: {df.shape}")

# =====================================
# SPLIT DATASET
# =====================================

print("\nCreating train-test split...")

X = df.drop(

    columns=[
        "Label",
        "Binary_Label"
    ]
)

y = df["Binary_Label"]

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42,

    stratify=y
)

print("Train-test split completed successfully")

print(f"\nX_train Shape: {X_train.shape}")

print(f"\nX_test Shape: {X_test.shape}")

# =====================================
# MODELS TO TUNE
# =====================================

models = {

    "XGBoost":

    XGBClassifier(

        random_state=42,

        eval_metric="logloss",

        use_label_encoder=False,

        n_jobs=-1
    ),

    "LightGBM":

    LGBMClassifier(

        random_state=42,

        n_jobs=-1
    )
}

# =====================================
# STORE RESULTS
# =====================================

results = []

# =====================================
# HYPERPARAMETER TUNING
# =====================================

print("\n=====================================")
print("STARTING HYPERPARAMETER TUNING")
print("=====================================")

for model_name, model in models.items():

    print(f"\nTuning {model_name}...")

    param_grid = PARAM_GRID[
        model_name
    ]

    random_search = RandomizedSearchCV(

        estimator=model,

        param_distributions=param_grid,

        n_iter=10,

        scoring="roc_auc",

        cv=3,

        verbose=2,

        random_state=42,

        n_jobs=-1
    )

    # =================================
    # TRAINING TIMER
    # =================================

    start_time = time.time()

    random_search.fit(

        X_train,

        y_train
    )

    end_time = time.time()

    training_time = (
        end_time - start_time
    )

    # =================================
    # BEST MODEL
    # =================================

    best_model = (
        random_search.best_estimator_
    )

    print(f"\nBest parameters for {model_name}:")

    print(
        random_search.best_params_
    )

    # =================================
    # PREDICTIONS
    # =================================

    print(f"\nGenerating predictions for {model_name}...")

    y_prob = best_model.predict_proba(
        X_test
    )[:, 1]

    # =================================
    # EVALUATION
    # =================================

    roc_auc = roc_auc_score(

        y_test,

        y_prob
    )

    print(f"\n{model_name} ROC-AUC: {round(roc_auc, 6)}")

    # =================================
    # SAVE MODEL
    # =================================

    model_path = (

        f"{MODEL_DIR}/"

        f"best_{model_name}.pkl"
    )

    joblib.dump(

        best_model,

        model_path
    )

    print(f"\n{model_name} model saved successfully")

    print(f"Saved Path: {model_path}")

    # =================================
    # STORE RESULTS
    # =================================

    results.append({

        "Model":
            model_name,

        "Best ROC AUC":
            round(roc_auc, 6),

        "Best Parameters":
            str(random_search.best_params_),

        "Training Time (s)":
            round(training_time, 2),

        "Saved Model Path":
            model_path
    })

    print("\n-------------------------------------")
    print(f"{model_name} tuning completed")
    print("-------------------------------------")

# =====================================
# CREATE RESULTS DATAFRAME
# =====================================

print("\nCreating tuning results dataframe...")

results_df = pd.DataFrame(
    results
)

# =====================================
# SORT RESULTS
# =====================================

results_df = results_df.sort_values(

    by="Best ROC AUC",

    ascending=False
)

# =====================================
# SAVE RESULTS
# =====================================

print("\nSaving tuning results...")

results_df.to_csv(

    RESULTS_PATH,

    index=False
)

print("Tuning results saved successfully")

print(f"\nResults Path:\n{RESULTS_PATH}")

# =====================================
# DISPLAY FINAL RESULTS
# =====================================

print("\n=====================================")
print("FINAL HYPERPARAMETER TUNING RESULTS")
print("=====================================\n")

print(results_df)

# =====================================
# BEST MODEL SUMMARY
# =====================================

best_model_name = (
    results_df.iloc[0]["Model"]
)

best_model_score = (
    results_df.iloc[0]["Best ROC AUC"]
)

print("\n=====================================")
print("BEST MODEL SELECTED")
print("=====================================")

print(f"\nBest Model: {best_model_name}")

print(f"\nBest ROC-AUC: {best_model_score}")

# =====================================
# PIPELINE COMPLETE
# =====================================

print("\n=====================================")
print("HYPERPARAMETER TUNING PIPELINE COMPLETE")
print("=====================================")

print("\nPipeline Achievements:")

print("- Dataset loaded successfully")

print("- Binary target engineering completed")

print("- Large-scale dataset sampling completed")

print("- Hyperparameter tuning executed")

print("- Multiple ensemble models benchmarked")

print("- Best production models exported")

print("- ROC-AUC optimization completed")

print("- Tuning results persisted successfully")