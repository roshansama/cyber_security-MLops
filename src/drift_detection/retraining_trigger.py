import pandas as pd


# =====================================
# Paths
# =====================================

PSI_RESULTS_PATH = (
    r"D:\MLOPS\data\processed"
    r"\psi_drift_results.csv"
)


# =====================================
# Drift Threshold
# =====================================

DRIFT_THRESHOLD = 0.25


# =====================================
# Load PSI Results
# =====================================

print("\nLoading PSI drift results...")

psi_df = pd.read_csv(
    PSI_RESULTS_PATH
)

print("PSI results loaded")


# =====================================
# Significant Drift Features
# =====================================

significant_drift = psi_df[
    psi_df['PSI Score'] > DRIFT_THRESHOLD
]

print("\n==============================")
print("DRIFT MONITORING REPORT")
print("==============================")


# =====================================
# Summary Statistics
# =====================================

total_features = len(psi_df)

drifted_features = len(
    significant_drift
)

max_psi = psi_df[
    'PSI Score'
].max()

avg_psi = psi_df[
    'PSI Score'
].mean()


print(f"\nTotal Features: {total_features}")

print(
    f"Significantly Drifted Features: "
    f"{drifted_features}"
)

print(f"\nMaximum PSI: {max_psi}")

print(f"\nAverage PSI: {avg_psi}")


# =====================================
# Top Drifted Features
# =====================================

print("\nTop Drifted Features:\n")

print(
    significant_drift[
        [
            'Feature',
            'PSI Score',
            'Drift Level'
        ]
    ].head(15)
)


# =====================================
# Retraining Logic
# =====================================

retrain_required = False

if drifted_features > 5:

    retrain_required = True

if max_psi > 0.5:

    retrain_required = True


# =====================================
# Decision Output
# =====================================

print("\n==============================")
print("RETRAINING DECISION")
print("==============================")


if retrain_required:

    print(
        "\nALERT: Significant drift detected"
    )

    print(
        "\nRetraining recommended"
    )

    print(
        "\nReason:"
    )

    print(
        "- High PSI feature drift"
    )

    print(
        "- Distribution instability"
    )

    print(
        "- Potential model degradation"
    )

else:

    print(
        "\nSystem stable"
    )

    print(
        "\nRetraining not required"
    )


# =====================================
# Simulated Pipeline Action
# =====================================

print("\n==============================")
print("PIPELINE ACTION")
print("==============================")


if retrain_required:

    print(
        "\nTriggering retraining pipeline..."
    )

    print(
        "\nSuggested Actions:"
    )

    print(
        "1. Retrain on latest traffic"
    )

    print(
        "2. Recalculate SHAP importance"
    )

    print(
        "3. Re-evaluate drift robustness"
    )

    print(
        "4. Deploy updated model"
    )

else:

    print(
        "\nContinue monitoring"
    )