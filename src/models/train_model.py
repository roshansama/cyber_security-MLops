from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def split_data(df):

    X = df.drop(
        columns=['Label', 'Binary_Label']
    )

    y = df['Binary_Label']

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


def train_random_forest(X_train, y_train):

    rf = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    rf.fit(X_train, y_train)

    return rf