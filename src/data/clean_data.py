import numpy as np


CONSTANT_COLUMNS = [
    'Bwd PSH Flags',
    'Bwd URG Flags',
    'Fwd Avg Bytes/Bulk',
    'Fwd Avg Packets/Bulk',
    'Fwd Avg Bulk Rate',
    'Bwd Avg Bytes/Bulk',
    'Bwd Avg Packets/Bulk',
    'Bwd Avg Bulk Rate'
]


def clean_dataset(df):

    # Replace infinite values
    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    # Remove missing values
    df.dropna(inplace=True)

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Fix corrupted labels
    df['Label'] = df['Label'].replace({
        'Web Attack � Brute Force':
            'Web Attack - Brute Force',

        'Web Attack � XSS':
            'Web Attack - XSS',

        'Web Attack � Sql Injection':
            'Web Attack - Sql Injection'
    })

    # Remove invalid negative values
    df = df[df['Flow Duration'] >= 0]

    df = df[df['min_seg_size_forward'] >= 0]

    # Remove constant features
    df.drop(
    columns=CONSTANT_COLUMNS,
    inplace=True,
    errors='ignore'
)

    return df