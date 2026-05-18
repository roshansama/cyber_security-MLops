import numpy as np


def validate_dataset(df, dataset_name):

    print(f"\nValidating {dataset_name}")

    print("\nShape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nInfinite Values:")
    print(
        np.isinf(
            df.select_dtypes(include=np.number)
        ).sum().sum()
    )

    print("\nLabel Distribution:")
    print(df['Label'].value_counts())