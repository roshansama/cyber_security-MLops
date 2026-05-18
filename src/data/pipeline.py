from src.data.load_data import load_dataset
from src.data.validate_data import validate_dataset
from src.data.clean_data import clean_dataset
from src.data.merge_data import merge_datasets


DATA_PATH = r"D:\MLOPS\data\raw"


def process_dataset(path, dataset_name):

    print(f"\nProcessing {dataset_name}")

    df = load_dataset(path)

    print("\nBefore Cleaning:")
    validate_dataset(df, dataset_name)

    df = clean_dataset(df)

    print("\nAfter Cleaning:")
    validate_dataset(df, f"{dataset_name} Cleaned")

    return df


def main():

    # Monday
    monday = process_dataset(
        rf"{DATA_PATH}\Monday-WorkingHours.pcap_ISCX.csv",
        "Monday"
    )

    # Tuesday
    tuesday = process_dataset(
        rf"{DATA_PATH}\Tuesday-WorkingHours.pcap_ISCX.csv",
        "Tuesday"
    )

    # Wednesday
    wednesday = process_dataset(
        rf"{DATA_PATH}\Wednesday-workingHours.pcap_ISCX.csv",
        "Wednesday"
    )

    # Thursday Morning
    thursday_morning = process_dataset(
        rf"{DATA_PATH}\Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv",
        "Thursday Morning"
    )

    # Thursday Afternoon
    thursday_afternoon = process_dataset(
        rf"{DATA_PATH}\Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv",
        "Thursday Afternoon"
    )

    # Merge Thursday
    thursday = merge_datasets([
        thursday_morning,
        thursday_afternoon
    ])

    # Friday Morning
    friday_morning = process_dataset(
        rf"{DATA_PATH}\Friday-WorkingHours-Morning.pcap_ISCX.csv",
        "Friday Morning"
    )

    # Friday PortScan
    friday_portscan = process_dataset(
        rf"{DATA_PATH}\Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv",
        "Friday PortScan"
    )

    # Friday DDoS
    friday_ddos = process_dataset(
        rf"{DATA_PATH}\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv",
        "Friday DDoS"
    )

    # Merge Friday
    friday = merge_datasets([
        friday_morning,
        friday_portscan,
        friday_ddos
    ])

    # Merge ALL
    final_df = merge_datasets([
        monday,
        tuesday,
        wednesday,
        thursday,
        friday
    ])

    print("\nFinal Dataset Shape:")
    print(final_df.shape)

    print("\nFinal Label Distribution:")
    print(final_df['Label'].value_counts())

    # Save processed dataset
    final_df.to_csv(
        r"D:\MLOPS\data\processed\cleaned_cicids2017.csv",
        index=False
    )

    # Save label distribution
    final_df['Label'].value_counts().to_csv(
        r"D:\MLOPS\data\processed\label_distribution.csv"
    )

    print("\nPipeline Completed Successfully")


if __name__ == "__main__":
    main()