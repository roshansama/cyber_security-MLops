def create_binary_target(df):

    df['Binary_Label'] = df['Label'].apply(
        lambda x: 0 if x == 'BENIGN' else 1
    )

    return df