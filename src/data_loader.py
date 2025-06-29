import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess_data(path="data/credit.csv"):
    # 1. Compute absolute CSV path relative to this script's directory
    base_dir = os.path.dirname(os.path.abspath(__file__))  # directory of this script
    csv_path = os.path.abspath(os.path.join(base_dir, "..", path))  # absolute path to csv

    # 2. Load data from CSV using the absolute path
    df = pd.read_csv(csv_path)

    # 3. Standardize column names: lowercase, underscores instead of spaces/hyphens
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('-', '_')
    )

    # 4. Remove unnecessary index column if present
    if 'unnamed:_0' in df.columns:
        df = df.drop(columns=['unnamed:_0'])

    # 5. Fill missing categorical columns or create them if missing (to ensure compatibility)
    cat_cols = ['sex', 'housing', 'saving_accounts', 'checking_account', 'purpose']
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].fillna('unknown')
        else:
            df[col] = 'unknown'  # create missing column with default 'unknown'

    # 6. Create target variable 'default' if not present (proxy label)
    if 'default' not in df.columns:
        df['default'] = ((df['credit_amount'] > 5000) & (df['duration'] > 24)).astype(int)

    # 7. Label encode categorical columns
    le = LabelEncoder()
    for col in cat_cols:
        if df[col].dtype == 'object':
            df[col] = le.fit_transform(df[col])

    # 8. Separate features and target variable
    X = df.drop('default', axis=1)
    y = df['default']

    # 9. Scale numeric features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 10. Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test