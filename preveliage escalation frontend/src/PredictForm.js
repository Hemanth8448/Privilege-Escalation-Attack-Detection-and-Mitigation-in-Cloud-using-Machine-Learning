import React, { useState } from "react";
import "./styles.css"; // Import CSS

const PredictForm = () => {
  const [formData, setFormData] = useState({
    Failed_Login_Attempts: 0,
    Anomaly_Score: 0.1,
    Session_Duration: 200,
    Concurrent_Sessions: 2,
    Keystroke_Anomaly: 0.05,
    Suspicious_Command_Execution: 0,
    Access_Control_Violation: 0,
    Network_Anomaly: 0,
    Time_Anomaly: 0,
  });

  const [result, setResult] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: parseFloat(e.target.value) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    setResult(data.prediction);
  };

  return (
    <div className="App">
      <h2>Privilege Escalation Attack Detection</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <div key={key}>
            <label>{key}: </label>
            <input
              type="number"
              name={key}
              value={formData[key]}
              onChange={handleChange}
              required
            />
          </div>
        ))}
        <button type="submit">Predict</button>
      </form>
      
      {result && (
        <h3 className={`result ${result === "Attack Found" ? "attack" : "no-attack"}`}>
          Result: {result}
        </h3>
      )}
    </div>
  );
};

export default PredictForm;