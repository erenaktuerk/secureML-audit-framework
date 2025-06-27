from sklearn.ensemble import RandomForestClassifier
import joblib
import mlflow

def train_model(X_train, y_train):
    mlflow.set_experiment("SecureML Credit Model")

    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Log model with MLflow
        mlflow.sklearn.log_model(model, "model")
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("model_type", "RandomForest")

        # Save model locally
        joblib.dump(model, "models/rf_model.joblib")

    return model