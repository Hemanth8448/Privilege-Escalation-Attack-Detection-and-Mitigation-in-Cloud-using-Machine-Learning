
# Privilege Escalation Attack Detection and Mitigation in Cloud Using Machine Learning

This project focuses on detecting privilege escalation attacks in cloud environments using machine learning algorithms. It includes data preprocessing, model training, REST API development with Flask, and frontend integration using ReactJS for real-time threat detection.

---
## Project Abstract
- Privilege escalation attacks in cloud environments pose significant security threats. 
- This project leverages machine learning techniques to detect and mitigate such attacks with high accuracy.
- Using feature selection, data augmentation, and advanced ML algorithms, the model classifies activities as 'Attack Found' or 'Not Found'. 
- An API is developed to integrate with a full-stack application, enabling real-time attack detection.


---

## Project Objectives

- Develop a machine learning model to accurately classify privilege escalation attack attempts.
- Boost cloud safety by spotting unusual behavior or warning signs that could mean someone’s trying to gain extra access they shouldn’t have.
- Optimize model performance using advanced feature selection and data augmentation techniques to improve detection accuracy.
-Integrate the system into a user-friendly full-stack application with an API for seamless real-time classification and deployment in cloud environments.
  

---

## Tech Stack

- **Backend:** Python, Flask, scikit-learn, XGBoost, LightGBM, CatBoost, joblib
- **Frontend:** ReactJS, HTML, CSS
- **Data Handling:** Pandas, NumPy, SMOTE
- **Visualization:** Matplotlib, Seaborn
- **Deployment:** Localhost / Cloud (AWS, Azure)

---

## Dataset Features

- `Failed_Login_Attempts`
- `Anomaly_Score`
- `Session_Duration`
- `Concurrent_Sessions`
- `Keystroke_Anomaly`
- `Suspicious_Command_Execution`
- `Access_Control_Violation`
- `Network_Anomaly`
- `Time_Anomaly`

Label:
- `Privilege_Escalation_Label`: `0` (Not Found), `1` (Attack Found)

---

## Project Structure

```
PRIVILEGE_ESCALATION_DETECTION/
│
├── privilege-escalation-frontend/        # Frontend React app
│   ├── public/
│   ├── src/
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── App.test.js
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── logo.svg
│   │   ├── PredictForm.js
│   │   ├── reportWebVitals.js
│   │   ├── setupTests.js
│   │   └── styles.css
│   ├── package.json
│   ├── package-lock.json
│   └── README.md
│
├── venv/                                 # Python virtual environment
│
├── app.py                                # Flask API backend
├── Final_proj.ipynb                      # Jupyter notebook for model training
├── privilege_escalation_augmented_dataset.csv  # Dataset file
├── privilege_escalation_model.pkl        # Trained model
├── scaler.pkl                            # Scaler for preprocessing
└── README.md                             # Root level README
```

---


# Next Steps to Run the Project

Follow the steps below to set up and run the Privilege Escalation Detection system:

## 1. Download Required Model Files
- Before running the backend, ensure that the privilege_escalation_model.pkl and scaler.pkl files are available in the project directory.
- You can generate and download these files by running shell commands directly from the Final_proj.ipynb notebook

## 2. Activate Python Environment & Start Backend

- Open a terminal in the project root directory.
- Activate your virtual environment:

```bash
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

- Start the Flask API backend:

```bash
python app.py
```

## 3. Install Frontend Dependencies (One-Time Setup)

- Navigate to the frontend project directory and install dependencies:

```bash
cd privilege-escalation-frontend
npm install
```

## 4. Run the Frontend React App

- To start the React frontend:

```bash
npm start
```

## 5. Verify Server URLs

- Flask Backend: `http://localhost:5000`
- React Frontend: `http://localhost:3000`

Ensure both servers are running simultaneously.

## 6. Check API Integration

- Make sure the frontend API call in `PredictForm.js` points to the correct Flask endpoint (`/predict`).

## 7. Confirm Model Files Exist

- Ensure the following files are present in the project root:
    - `privilege_escalation_model.pkl` — Trained ML model.
    - `scaler.pkl` — Scaler used for feature normalization.

These files should be properly loaded in `app.py` for predictions.


## How It Works

1. User inputs security log data into the web form.
2. Data is sent to the Flask API via POST request.
3. Model predicts if the input indicates an attack.
4. The result is returned and displayed on the interface.

---

## Model Performance

- Final Accuracy: **87%**
- Techniques Used:
  - SMOTE for data balancing
  - Feature selection (SHAP, RFE)
  - Models: Random Forest, XGBoost, LightGBM, CatBoost, Gradient Boosting
  - TPOT and GridSearchCV for hyperparameter tuning

---

