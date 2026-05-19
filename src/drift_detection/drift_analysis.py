import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# FILE PATHS
# =====================================

DATA_PATH = (
    "data/processed/drift_dataset.csv"
)

OUTPUT_PATH = (
    "data/processed/psi_drift_results.csv"
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
# CREATE REFERENCE & CURRENT DATA
# =====================================

print("\nCreating reference and current distributions...")

reference_data = df[
    df["Day"].isin([
        "Monday",
        "Tuesday"
    ])
]

current_data = df[
    df["Day"] == "Friday"
]

print("\nReference Dataset Shape:")
print(reference_data.shape)

print("\nCurrent Dataset Shape:")
print(current_data.shape)

# =====================================
# NUMERIC FEATURES ONLY
# =====================================

print("\nExtracting numeric features...")

numeric_columns = df.select_dtypes(

    include=[
        "int64",
        "float64"
    ]

).columns.tolist()

# =====================================
# REMOVE TARGET COLUMNS
# =====================================

remove_columns = [

    "Binary_Label"
]

for col in remove_columns:

    if col in numeric_columns:

        numeric_columns.remove(col)

print(f"\nTotal Numeric Features: {len(numeric_columns)}")

# =====================================
# PSI CALCULATION FUNCTION
# =====================================

def calculate_psi(
    expected,
    actual,
    buckets=10
):

    expected = np.array(expected)

    actual = np.array(actual)

    # =================================
    # REMOVE NaN VALUES
    # =================================

    expected = expected[
        ~np.isnan(expected)
    ]

    actual = actual[
        ~np.isnan(actual)
    ]

    # =================================
    # CREATE BREAKPOINTS
    # =================================

    breakpoints = np.percentile(

        expected,

        np.arange(
            0,
            101,
            100 / buckets
        )
    )

    breakpoints = np.unique(
        breakpoints
    )

    # =================================
    # SAFETY CHECK
    # =================================

    if len(breakpoints) <= 2:

        return 0

    # =================================
    # HISTOGRAM COUNTS
    # =================================

    expected_counts = np.histogram(

        expected,

        bins=breakpoints
    )[0]

    actual_counts = np.histogram(

        actual,

        bins=breakpoints
    )[0]

    # =================================
    # PERCENTAGES
    # =================================

    expected_percents = (
        expected_counts / len(expected)
    )

    actual_percents = (
        actual_counts / len(actual)
    )

    # =================================
    # PREVENT DIVISION ERRORS
    # =================================

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

    # =================================
    # PSI FORMULA
    # =================================

    psi_values = (

        expected_percents
        -
        actual_percents

    ) * np.log(

        expected_percents
        /
        actual_percents
    )

    psi_total = np.sum(
        psi_values
    )

    return psi_total

# =====================================
# CALCULATE PSI FOR ALL FEATURES
# =====================================

print("\nCalculating PSI scores...")

results = []

for feature in numeric_columns:

    try:

        psi_score = calculate_psi(

            reference_data[feature],

            current_data[feature]
        )

        # =============================
        # DRIFT INTERPRETATION
        # =============================

        if psi_score < 0.1:

            drift_level = "No Drift"

        elif psi_score < 0.25:

            drift_level = "Moderate Drift"

        else:

            drift_level = "Significant Drift"

        results.append({

            "Feature":
                feature,

            "PSI Score":
                round(psi_score, 6),

            "Drift Level":
                drift_level
        })

        print(

            f"{feature} "
            f"-> PSI: {round(psi_score, 4)} "
            f"({drift_level})"
        )

    except Exception as e:

        print(

            f"\nError processing "
            f"{feature}: {e}"
        )

# =====================================
# CREATE RESULTS DATAFRAME
# =====================================

print("\nCreating results dataframe...")

results_df = pd.DataFrame(
    results
)

results_df = results_df.sort_values(

    by="PSI Score",

    ascending=False
)

# =====================================
# SAVE RESULTS
# =====================================

print("\nSaving PSI drift results...")

results_df.to_csv(

    OUTPUT_PATH,

    index=False
)

print("PSI drift results saved successfully")

print(f"\nResults saved at:\n{OUTPUT_PATH}")

# =====================================
# DISPLAY TOP DRIFTED FEATURES
# =====================================

print("\n=====================================")
print("TOP DRIFTED FEATURES")
print("=====================================\n")

print(
    results_df.head(20)
)

# =====================================
# DRIFT SUMMARY
# =====================================

significant_drift_count = (

    results_df[
        results_df["Drift Level"]
        ==
        "Significant Drift"
    ]

    .shape[0]
)

moderate_drift_count = (

    results_df[
        results_df["Drift Level"]
        ==
        "Moderate Drift"
    ]

    .shape[0]
)

print("\n=====================================")
print("DRIFT SUMMARY")
print("=====================================")

print(
    f"\nSignificant Drift Features: "
    f"{significant_drift_count}"
)

print(
    f"\nModerate Drift Features: "
    f"{moderate_drift_count}"
)

# =====================================
# VISUALIZATION
# =====================================

print("\nGenerating drift visualization...")

top_features = results_df.head(10)

plt.figure(
    figsize=(14, 7)
)

plt.bar(

    top_features["Feature"],

    top_features["PSI Score"]
)

plt.xticks(
    rotation=90
)

plt.ylabel(
    "PSI Score"
)

plt.xlabel(
    "Features"
)

plt.title(
    "Top 10 Drifted Features"
)

plt.tight_layout()

plt.show()

# =====================================
# PIPELINE COMPLETE
# =====================================

print("\n=====================================")
print("DRIFT ANALYSIS PIPELINE COMPLETE")
print("=====================================")