from sklearn.ensemble import RandomForestClassifier
import joblib
import mlflow
import os

def train_model(X_train, y_train):
    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Log model with input example (first 5 rows)
        mlflow.sklearn.log_model(
            model, 
            "model", 
            input_example=X_train.iloc[:5] if hasattr(X_train, "iloc") else X_train[:5]
        )
        mlflow.log_param("n_estimators", 100)
        mlflow.log_param("model_type", "RandomForest")

        # Save model locally
        joblib.dump(model, "models/rf_model.joblib")

    return model