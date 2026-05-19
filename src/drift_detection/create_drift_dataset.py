import pandas as pd

from src.data.clean_data import (
    clean_dataset
)

# =====================================
# FILE PATHS
# =====================================

MONDAY_PATH = (
    "data/raw/Monday-WorkingHours.pcap_ISCX.csv"
)

TUESDAY_PATH = (
    "data/raw/Tuesday-WorkingHours.pcap_ISCX.csv"
)

WEDNESDAY_PATH = (
    "data/raw/Wednesday-workingHours.pcap_ISCX.csv"
)

THURSDAY_MORNING_PATH = (
    "data/raw/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"
)

THURSDAY_AFTERNOON_PATH = (
    "data/raw/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv"
)

FRIDAY_MORNING_PATH = (
    "data/raw/Friday-WorkingHours-Morning.pcap_ISCX.csv"
)

FRIDAY_DDOS_PATH = (
    "data/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
)

FRIDAY_PORTSCAN_PATH = (
    "data/raw/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv"
)

# =====================================
# LOAD DATASETS
# =====================================

print("\nLoading datasets...")

monday = pd.read_csv(
    MONDAY_PATH
)

tuesday = pd.read_csv(
    TUESDAY_PATH
)

wednesday = pd.read_csv(
    WEDNESDAY_PATH
)

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

print("Datasets loaded successfully")

# =====================================
# STANDARDIZE COLUMN NAMES
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

print("\nStandardizing column names...")

for dataset in datasets:

    dataset.columns = (
        dataset.columns
        .str.strip()
    )

print("Column names standardized")

# =====================================
# ADD DAY METADATA
# =====================================

print("\nAdding day metadata...")

monday["Day"] = "Monday"

tuesday["Day"] = "Tuesday"

wednesday["Day"] = "Wednesday"

thursday_morning["Day"] = "Thursday"

thursday_afternoon["Day"] = "Thursday"

friday_morning["Day"] = "Friday"

friday_ddos["Day"] = "Friday"

friday_portscan["Day"] = "Friday"

print("Day metadata added")

# =====================================
# MERGE SAME-DAY FILES
# =====================================

print("\nMerging same-day datasets...")

thursday = pd.concat(

    [

        thursday_morning,
        thursday_afternoon
    ],

    ignore_index=True
)

friday = pd.concat(

    [

        friday_morning,
        friday_ddos,
        friday_portscan
    ],

    ignore_index=True
)

print("Same-day datasets merged")

# =====================================
# COMBINE ALL DAYS
# =====================================

print("\nCombining all datasets...")

df = pd.concat(

    [

        monday,
        tuesday,
        wednesday,
        thursday,
        friday
    ],

    ignore_index=True
)

print("All datasets combined successfully")

# =====================================
# DATASET SHAPE BEFORE CLEANING
# =====================================

print(f"\nRaw Dataset Shape: {df.shape}")

# =====================================
# CLEAN DATASET
# =====================================

print("\nCleaning dataset...")

df = clean_dataset(df)

print("Dataset cleaned successfully")

# =====================================
# DATASET SHAPE AFTER CLEANING
# =====================================

print(f"\nCleaned Dataset Shape: {df.shape}")

# =====================================
# SAVE DRIFT DATASET
# =====================================

OUTPUT_PATH = (
    "data/processed/drift_dataset.csv"
)

print("\nSaving drift dataset...")

df.to_csv(

    OUTPUT_PATH,

    index=False
)

print("Drift dataset saved successfully")

# =====================================
# FINAL SUMMARY
# =====================================

print("\n=====================================")
print("DRIFT DATASET PIPELINE COMPLETE")
print("=====================================")

print(f"\nFinal Dataset Shape: {df.shape}")

print(f"\nDataset saved at:\n{OUTPUT_PATH}")