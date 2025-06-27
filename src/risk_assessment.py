def classify_model_risk(purpose, sensitive_features):
    if purpose == "credit_scoring" and "Sex" in sensitive_features:
        return "High Risk (EU AI Act – Annex III)"
    return "Moderate Risk"


def detect_bias(X, y, sensitive_feature, model):
    import pandas as pd
    from sklearn.metrics import accuracy_score

    bias_report = {}
    groups = X[sensitive_feature].unique()

    for group in groups:
        group_idx = X[sensitive_feature] == group
        group_acc = accuracy_score(y[group_idx], model.predict(X[group_idx]))
        bias_report[group] = round(group_acc, 3)

    return bias_report