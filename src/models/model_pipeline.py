import pandas as pd

from src.features.build_features import (
    create_binary_target
)

from src.models.train_model import (
    split_data,
    train_random_forest
)

from src.models.evaluate_model import (
    evaluate_model,
    get_feature_importance
)

# =====================================
# FILE PATH
# =====================================

DATA_PATH = "data/processed/cleaned_cicids2017.csv"


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

print("\nCreating binary target column...")

df = create_binary_target(
    df
)

print("Binary target created successfully")

# =====================================
# TRAIN / TEST SPLIT
# =====================================

print("\nSplitting dataset into train and test sets...")

X_train, X_test, y_train, y_test = split_data(
    df
)

print("\nTrain/Test split completed")

print(f"\nX_train Shape: {X_train.shape}")

print(f"\nX_test Shape: {X_test.shape}")

# =====================================
# MODEL TRAINING
# =====================================

print("\nTraining Random Forest model...")

model = train_random_forest(

    X_train,

    y_train
)

print("Random Forest model trained successfully")

# =====================================
# MODEL EVALUATION
# =====================================

print("\n=====================================")
print("MODEL EVALUATION")
print("=====================================")

evaluate_model(

    model,

    X_test,

    y_test
)

# =====================================
# FEATURE IMPORTANCE
# =====================================

print("\nGenerating feature importance rankings...")

feature_importance = get_feature_importance(

    model,

    X_train
)

print("\n=====================================")
print("TOP 20 IMPORTANT FEATURES")
print("=====================================\n")

print(
    feature_importance.head(20)
)

# =====================================
# PIPELINE COMPLETE
# =====================================

print("\n=====================================")
print("RANDOM FOREST PIPELINE COMPLETE")
print("=====================================")

print("\nPipeline Summary:")

print("- Processed dataset loaded")

print("- Binary target engineering completed")

print("- Dataset split into training/testing sets")

print("- Random Forest model trained")

print("- Evaluation metrics generated")

print("- Feature importance analysis completed")