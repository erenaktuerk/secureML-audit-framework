import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess_data(path="data/credit.csv"):
    # 1. Daten laden
    df = pd.read_csv(path)

    # 2. Spaltennamen standardisieren (snake_case)
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('-', '_')
    )

    # 3. Falls Index-Spalte 'unnamed: 0' existiert, löschen
    if 'unnamed:_0' in df.columns:
        df = df.drop(columns=['unnamed:_0'])

    # 4. Fehlende Werte in kategorischen Variablen auffüllen
    cat_cols = ['sex', 'housing', 'saving_accounts', 'checking_account', 'purpose']
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].fillna('unknown')
        else:
            raise KeyError(f"Spalte '{col}' fehlt in den Daten.")

    # 5. Zielvariable 'default' prüfen
    if 'default' not in df.columns:
        # Beispiel-Definition, falls noch nicht vorhanden
        df['default'] = ((df['credit_amount'] > 5000) & (df['duration'] > 24)).astype(int)

    # 6. Label Encoding für kategorische Variablen
    le = LabelEncoder()
    for col in cat_cols:
        df[col] = le.fit_transform(df[col])

    # 7. Features und Ziel trennen
    X = df.drop('default', axis=1)
    y = df['default']

    # 8. Numerische Features skalieren
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # 9. Daten aufteilen
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test