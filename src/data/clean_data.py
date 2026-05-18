import numpy as np


def clean_dataset(df):

    # Replace infinities
    df.replace(
        [np.inf, -np.inf],
        np.nan,
        inplace=True
    )

    # Remove missing values
    df.dropna(inplace=True)

    # Remove duplicates
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

    return df