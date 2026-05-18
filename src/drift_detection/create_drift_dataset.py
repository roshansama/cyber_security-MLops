import pandas as pd

from src.data.clean_data import (
    clean_dataset
)


# =====================================
# File Paths
# =====================================

MONDAY_PATH = (
    r"D:\MLOPS\data\raw"
    r"\Monday-WorkingHours.pcap_ISCX.csv"
)

TUESDAY_PATH = (
    r"D:\MLOPS\data\raw"
    r"\Tuesday-WorkingHours.pcap_ISCX.csv"
)

WEDNESDAY_PATH = (
    r"D:\MLOPS\data\raw"
    r"\Wednesday-workingHours.pcap_ISCX.csv"
)

THURSDAY_MORNING_PATH = (
    r"D:\MLOPS\data\raw"
    r"\Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"
)

THURSDAY_AFTERNOON_PATH = (
    r"D:\MLOPS\data\raw"
    r"\Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv"
)

FRIDAY_MORNING_PATH = (
    r"D:\MLOPS\data\raw"
    r"\Friday-WorkingHours-Morning.pcap_ISCX.csv"
)

FRIDAY_DDOS_PATH = (
    r"D:\MLOPS\data\raw"
    r"\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
)

FRIDAY_PORTSCAN_PATH = (
    r"D:\MLOPS\data\raw"
    r"\Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv"
)


# =====================================
# Load Datasets
# =====================================

print("\nLoading datasets...")


monday = pd.read_csv(MONDAY_PATH)

tuesday = pd.read_csv(TUESDAY_PATH)

wednesday = pd.read_csv(WEDNESDAY_PATH)

thursday_morning = pd.read_csv(
    THURSDAY_MORNING_PATH
)

thursday_afternoon = pd.read_csv(
    THURSDAY_AFTERNOON_PATH
)

friday_morning = pd.read_csv(
    FRIDAY_MORNING_PATH
)

friday_ddos = pd.read_csv(
    FRIDAY_DDOS_PATH
)

friday_portscan = pd.read_csv(
    FRIDAY_PORTSCAN_PATH
)

print("Datasets loaded")


# =====================================
# Standardize Column Names
# =====================================

datasets = [

    monday,
    tuesday,
    wednesday,
    thursday_morning,
    thursday_afternoon,
    friday_morning,
    friday_ddos,
    friday_portscan
]

for dataset in datasets:

    dataset.columns = (
        dataset.columns
        .str.strip()
    )

# =====================================
# Add Day Metadata
# =====================================

monday['Day'] = 'Monday'

tuesday['Day'] = 'Tuesday'

wednesday['Day'] = 'Wednesday'

thursday_morning['Day'] = 'Thursday'

thursday_afternoon['Day'] = 'Thursday'

friday_morning['Day'] = 'Friday'

friday_ddos['Day'] = 'Friday'

friday_portscan['Day'] = 'Friday'


# =====================================
# Merge Same-Day Files
# =====================================

thursday = pd.concat([
    thursday_morning,
    thursday_afternoon
])

friday = pd.concat([
    friday_morning,
    friday_ddos,
    friday_portscan
])


# =====================================
# Combine All Days
# =====================================

print("\nCombining datasets...")

df = pd.concat([

    monday,
    tuesday,
    wednesday,
    thursday,
    friday

])

print("Datasets combined")


# =====================================
# Clean Dataset
# =====================================

print("\nCleaning dataset...")

df = clean_dataset(df)

print("Dataset cleaned")


# =====================================
# Save Drift Dataset
# =====================================

OUTPUT_PATH = (
    r"D:\MLOPS\data\processed"
    r"\drift_dataset.csv"
)

df.to_csv(
    OUTPUT_PATH,
    index=False
)

print("\nDrift dataset saved")

print(f"\nFinal Shape: {df.shape}")

print(
    f"\nDataset saved at:\n"
    f"{OUTPUT_PATH}"
)