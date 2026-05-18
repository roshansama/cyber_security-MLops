import pandas as pd


def merge_datasets(dataset_list):

    merged_df = pd.concat(
        dataset_list,
        ignore_index=True
    )

    return merged_df