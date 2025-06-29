from sklearn.ensemble import RandomForestClassifier
import joblib
import mlflow
import os

def train_model(X_train, y_train):
    # Basisverzeichnis berechnen
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Pfad zum lokalen Speicherort für Modelle
    models_dir = os.path.join(base_dir, "..", "models")
    os.makedirs(models_dir, exist_ok=True)  # Ordner erstellen, falls nicht vorhanden

    # Lokalen Tracking-Pfad für MLflow setzen
    tracking_dir = os.path.join(base_dir, "..", "mlruns")
    mlflow.set_tracking_uri(f"file:///{tracking_dir.replace(os.sep, '/')}")

    # Experiment explizit setzen oder anlegen (wichtig, um Fehler mit Experiment-ID 0 zu vermeiden)
    experiment_name = "SecureML_Experiment"
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        mlflow.sklearn.log_model(
            model,
            name="model",
            input_example=X_train[:5]
        )
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("model_type", "RandomForest")

        # Lokale Speicherung des Modells
        model_path = os.path.join(models_dir, "rf_model.joblib")
        joblib.dump(model, model_path)

    return model