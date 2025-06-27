import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess_data(path="data/credit.csv"):
    # Load dataset
    df = pd.read_csv(path)

    # Drop unnamed index column if exists
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    # Create synthetic target variable for demo purposes
    # Assumption: credit amount > 5000 AND duration > 24 → risk = 1 (bad credit)
    df["default"] = ((df["Credit amount"] > 5000) & (df["Duration"] > 24)).astype(int)

    # Categorical columns
    cat_cols = ["Sex", "Housing", "Saving accounts", "Checking account", "Purpose"]
    for col in cat_cols:
        df[col] = df[col].fillna("unknown")
        df[col] = LabelEncoder().fit_transform(df[col])

    # Features / Target
    X = df.drop("default", axis=1)
    y = df["default"]

    # Scaling numeric features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test