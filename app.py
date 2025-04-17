from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import joblib


# Load trained model and scaler
model = joblib.load("privilege_escalation_model.pkl")
scaler = joblib.load("scaler.pkl")

# Define Flask App
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Define API Endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.json  
        
        # Convert JSON to DataFrame
        df = pd.DataFrame([data])

        # Feature Engineering
        df["Login_Anomaly_Score"] = df["Failed_Login_Attempts"] * df["Anomaly_Score"]
        df["Session_Keystroke_Anomaly"] = df["Session_Duration"] * df["Keystroke_Anomaly"]
        df["Anomaly_Ratio"] = df["Failed_Login_Attempts"] / (df["Concurrent_Sessions"] + 1)

        # Selected Features
        selected_features = [
            "Failed_Login_Attempts", "Anomaly_Score", "Session_Duration", "Concurrent_Sessions",
            "Keystroke_Anomaly", "Suspicious_Command_Execution", "Access_Control_Violation",
            "Network_Anomaly", "Time_Anomaly", "Login_Anomaly_Score", "Session_Keystroke_Anomaly", "Anomaly_Ratio"
        ]

        # Apply Scaling
        X_scaled = scaler.transform(df[selected_features])

        # Make Prediction
        prediction = model.predict(X_scaled)[0]

        # Return Result
        result = "Attack Found" if prediction == 1 else "Attack Not Found"
        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": str(e)})

# Run the Flask App
if __name__ == '__main__':
    app.run(debug=True)
