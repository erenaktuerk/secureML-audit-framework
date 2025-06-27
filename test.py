import pandas as pd

# Rohdaten laden
df = pd.read_csv('data/credit.csv')

# Neue Zielvariable basierend auf plausibler Risikologik erstellen
def create_default_label(row):
    if row['Credit amount'] > 5000:
        return 1
    if row['Duration'] > 36:
        return 1
    if pd.isna(row['Checking account']) or row['Checking account'] == 'little':
        return 1
    return 0

# Zielvariable berechnen
df['default'] = df.apply(create_default_label, axis=1)

# Verteilung anzeigen zur Kontrolle
print("Verteilung der Zielvariable:")
print(df['default'].value_counts(normalize=True).rename(lambda x: f"default = {x}"))

# Neue Datei speichern
df.to_csv('data/processed_data.csv', index=False)
print("\nZielvariable erfolgreich erstellt und gespeichert in: data/processed_data.csv")