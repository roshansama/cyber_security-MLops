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

import pandas as pd


DATA_PATH = (
    r"D:\MLOPS\data\processed"
    r"\cleaned_cicids2017.csv"
)


# Load processed dataset
df = pd.read_csv(DATA_PATH)


# Create binary target
df = create_binary_target(df)


# Split dataset
X_train, X_test, y_train, y_test = split_data(df)


# Train model
model = train_random_forest(
    X_train,
    y_train
)


# Evaluate model
evaluate_model(
    model,
    X_test,
    y_test
)


# Feature importance
feature_importance = get_feature_importance(
    model,
    X_train
)

print("\nTop 20 Important Features:\n")

print(
    feature_importance.head(20)
)