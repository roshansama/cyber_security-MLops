import time
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


# Load processed dataset
DATA_PATH = (
    r"D:\MLOPS\data\processed"
    r"\cleaned_cicids2017.csv"
)

df = pd.read_csv(DATA_PATH)


# Create binary target
df = create_binary_target(df)


# Split data
X_train, X_test, y_train, y_test = split_data(df)


# Load models
models = get_models()


# Store results
results = []


# Train and evaluate models
for model_name, model in models.items():

    print(f"\nTraining {model_name}...")

    start_time = time.time()

    # Train model
    model.fit(X_train, y_train)

    end_time = time.time()

    training_time = end_time - start_time

    # Predictions
    y_pred = model.predict(X_test)

    # Probability predictions
    y_prob = model.predict_proba(X_test)[:, 1]

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(y_test, y_pred)

    recall = recall_score(y_test, y_pred)

    f1 = f1_score(y_test, y_pred)

    roc_auc = roc_auc_score(y_test, y_prob)

    # Save results
    results.append({
        "Model": model_name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1,
        "ROC AUC": roc_auc,
        "Training Time (s)": training_time
    })

    print(f"{model_name} Completed")


# Convert to DataFrame
results_df = pd.DataFrame(results)


# Sort by ROC-AUC
results_df = results_df.sort_values(
    by="ROC AUC",
    ascending=False
)


# Display results
print("\nModel Comparison Results:\n")

print(results_df)


# Save results
results_df.to_csv(
    r"D:\MLOPS\data\processed\model_comparison_results.csv",
    index=False
)