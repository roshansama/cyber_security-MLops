import joblib
import shap
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from src.features.build_features import (
    create_binary_target
)


# =====================================
# Paths
# =====================================

DATA_PATH = (
    r"D:\MLOPS\data\processed"
    r"\cleaned_cicids2017.csv"
)

MODEL_PATH = (
    r"D:\MLOPS\models"
    r"\best_XGBoost.pkl"
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
# Sample Dataset
# =====================================

print("\nSampling dataset for SHAP...")

df = df.sample(
    n=10000,
    random_state=42
)

print("Dataset sampled")


# =====================================
# Split Dataset
# =====================================

X = df.drop(
    columns=['Label', 'Binary_Label']
)

y = df['Binary_Label']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Train-test split completed")


# =====================================
# Load Model
# =====================================

print("\nLoading trained model...")

model = joblib.load(MODEL_PATH)

print("Model loaded")


# =====================================
# Create SHAP Explainer
# =====================================

print("\nCreating SHAP explainer...")

explainer = shap.TreeExplainer(model)

print("Explainer created")


# =====================================
# Generate SHAP Values
# =====================================

print("\nGenerating SHAP values...")

shap_values = explainer.shap_values(X_test)

print("SHAP values generated")


# =====================================
# SHAP Summary Plot
# =====================================

print("\nDisplaying SHAP summary plot...")

shap.summary_plot(
    shap_values,
    X_test
)


# =====================================
# SHAP Bar Plot
# =====================================

print("\nDisplaying SHAP feature importance plot...")

shap.summary_plot(
    shap_values,
    X_test,
    plot_type="bar"
)


# =====================================
# SHAP Force Plot
# =====================================

print("\nGenerating SHAP force plot...")

shap.initjs()

force_plot = shap.force_plot(
    explainer.expected_value,
    shap_values[0],
    X_test.iloc[0]
)

print(force_plot)


# =====================================
# Dependence Plot
# =====================================

TOP_FEATURE = "Bwd Packet Length Std"

print(
    f"\nGenerating dependence plot "
    f"for {TOP_FEATURE}..."
)

shap.dependence_plot(
    TOP_FEATURE,
    shap_values,
    X_test
)