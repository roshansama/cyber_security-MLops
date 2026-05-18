import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# =====================================
# Paths
# =====================================

DATA_PATH = (
    r"D:\MLOPS\data\processed"
    r"\drift_dataset.csv"
)

OUTPUT_PATH = (
    r"D:\MLOPS\data\processed"
    r"\psi_drift_results.csv"
)


# =====================================
# Load Dataset
# =====================================

print("\nLoading drift dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset loaded")


# =====================================
# Create Reference & Current Data
# =====================================

reference_data = df[
    df['Day'].isin([
        'Monday',
        'Tuesday'
    ])
]

current_data = df[
    df['Day'] == 'Friday'
]

print("\nReference Shape:")
print(reference_data.shape)

print("\nCurrent Shape:")
print(current_data.shape)


# =====================================
# Numeric Features Only
# =====================================

numeric_columns = df.select_dtypes(
    include=[
        'int64',
        'float64'
    ]
).columns.tolist()

# Remove target if needed
if 'Binary_Label' in numeric_columns:
    numeric_columns.remove('Binary_Label')


# =====================================
# PSI Function
# =====================================

def calculate_psi(
    expected,
    actual,
    buckets=10
):

    expected = np.array(expected)

    actual = np.array(actual)

    breakpoints = np.percentile(
        expected,
        np.arange(0, 101, 100 / buckets)
    )

    breakpoints = np.unique(
        breakpoints
    )

    expected_counts = np.histogram(
        expected,
        bins=breakpoints
    )[0]

    actual_counts = np.histogram(
        actual,
        bins=breakpoints
    )[0]

    expected_percents = (
        expected_counts / len(expected)
    )

    actual_percents = (
        actual_counts / len(actual)
    )

    # Prevent division by zero
    expected_percents = np.where(
        expected_percents == 0,
        0.0001,
        expected_percents
    )

    actual_percents = np.where(
        actual_percents == 0,
        0.0001,
        actual_percents
    )

    psi_values = (
        expected_percents - actual_percents
    ) * np.log(
        expected_percents / actual_percents
    )

    psi_total = np.sum(
        psi_values
    )

    return psi_total


# =====================================
# Calculate PSI For Features
# =====================================

results = []

print("\nCalculating PSI scores...")


for feature in numeric_columns:

    try:

        psi_score = calculate_psi(

            reference_data[feature],

            current_data[feature]
        )

        # Drift interpretation
        if psi_score < 0.1:

            drift_level = "No Drift"

        elif psi_score < 0.25:

            drift_level = "Moderate Drift"

        else:

            drift_level = "Significant Drift"

        results.append({

            "Feature": feature,

            "PSI Score": psi_score,

            "Drift Level": drift_level
        })

    except Exception as e:

        print(
            f"Error processing "
            f"{feature}: {e}"
        )


# =====================================
# Results DataFrame
# =====================================

results_df = pd.DataFrame(results)

results_df = results_df.sort_values(
    by='PSI Score',
    ascending=False
)


# =====================================
# Save Results
# =====================================

results_df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\nPSI drift results saved")

print(
    f"\nResults saved at:\n"
    f"{OUTPUT_PATH}"
)


# =====================================
# Display Top Drift Features
# =====================================

print("\nTop Drifted Features:\n")

print(
    results_df.head(20)
)


# =====================================
# Visualization
# =====================================

top_features = results_df.head(10)

plt.figure(figsize=(12, 6))

plt.bar(
    top_features['Feature'],
    top_features['PSI Score']
)

plt.xticks(
    rotation=90
)

plt.ylabel("PSI Score")

plt.title(
    "Top 10 Drifted Features"
)

plt.tight_layout()

plt.show()