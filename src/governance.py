import mlflow
import shap
import matplotlib.pyplot as plt
import json
import os
from datetime import datetime

def log_model_metadata(model_name, version, data_source, owner, purpose):
    metadata = {
        "model_name": model_name,
        "version": version,
        "data_source": data_source,
        "owner": owner,
        "purpose": purpose,
        "timestamp": datetime.utcnow().isoformat()
    }

    os.makedirs("reports", exist_ok=True)
    with open("reports/model_metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)

    print("Model metadata logged.")


def generate_audit_entry(model_name, risk_level, bias):
    audit = {
        "model": model_name,
        "risk_classification": risk_level,
        "bias_detection": bias,
        "timestamp": datetime.utcnow().isoformat()
    }

    os.makedirs("reports", exist_ok=True)
    with open("reports/audit_log.json", "w") as f:
        json.dump(audit, f, indent=4)

    print("Audit entry generated.")