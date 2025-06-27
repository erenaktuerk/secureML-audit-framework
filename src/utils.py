import joblib

def save_model(model, path="models/model.joblib"):
    joblib.dump(model, path)

def load_model(path="models/model.joblib"):
    return joblib.load(path)

def load_metrics():
    return {
        "accuracy": 0.89,
        "bias_score": 0.03,
        "risk_level": "Moderate"
    }