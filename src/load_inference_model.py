import os

import mlflow.pytorch
from mlflow.tracking import MlflowClient

MODEL_NAME = "LoanPayback"


def load_production_model():
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000"))
    model_uri = f"models:/{MODEL_NAME}/Production"
    model = mlflow.pytorch.load_model(model_uri)
    model.eval()
    client = MlflowClient()
    versions = client.get_latest_versions(MODEL_NAME, stages=["Production"])

    # if model is loaded successfully, return the model, version, model_uri, model_name
    if model:
        return {
            "status_code": 200,
            "message": "Model loaded successfully",
            "model": model,
            "version": int(versions[0].version),
            "model_uri": model_uri,
            "model_name": MODEL_NAME,
        }
    else:
        return {"status_code": 500, "message": "Failed to load model"}
