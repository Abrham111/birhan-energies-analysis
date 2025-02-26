# Brent Oil Price Analysis and Prediction

## Project Overview
This project analyzes Brent crude oil prices using **time series models** and **machine learning**. It includes:
- **Data Collection & Preprocessing**: Fetching, cleaning, and preparing historical oil price data.
- **Exploratory Data Analysis (EDA)**: Statistical summaries and visualizations.
- **Feature Engineering**: Creating meaningful features for modeling.
- **Predictive Modeling**:
  - **LSTM (Long Short-Term Memory)**: Predicts future oil prices.
  - **GARCH (Generalized Autoregressive Conditional Heteroskedasticity)**: Forecasts oil price volatility.
- **Deployment**:
  - **Backend (Flask API)**: Provides endpoints for predictions and data.
  - **Frontend (React + TailwindCSS)**: Displays an interactive dashboard with charts and insights.

---

## Tech Stack
### **Backend (Flask API)**
- Flask
- Pandas
- NumPy
- Scikit-learn
- TensorFlow/Keras (for LSTM)
- arch (for GARCH modeling)

### **Frontend (React + TailwindCSS)**
- React.js
- Recharts (for data visualization)
- Axios (for API requests)
- TailwindCSS (for styling)

---

## Installation & Setup

### **Backend (Flask API)**
#### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

#### 2. Run Flask API
```bash
python app.py
```
API runs at: **`http://127.0.0.1:5000/`**

#### **Available API Endpoints**
| Endpoint        | Description |
|----------------|-------------|
| `/api/data`    | Returns historical price data |
| `/api/summary` | Provides key statistics (max, min, avg price) |

---

### **Frontend (React + TailwindCSS)**
#### 1. Install Dependencies
```bash
cd DataDashboard
npm install
```

#### 2. Run DataDashboard
```bash
npm start
```
Frontend runs at: **`(http://localhost:5173/)`**

---

## Feature Engineering
- Created **Log returns** for GARCH modeling.
- Used **rolling averages** and **trend indicators** for better LSTM performance.

---

## Model Training & Evaluation
### **LSTM Model** (Deep Learning)
- Input: **Last 10 days of prices**
- Output: **Predicted price**
- Loss function: **Mean Squared Error (MSE)**
- Optimizer: **Adam**
- Evaluation: **Root Mean Squared Error (RMSE), MAE**

### **GARCH Model** (Statistical Modeling)
- Input: **Log returns** of oil prices
- Output: **Predicted volatility**
- Used: **GARCH(1,1)**
- Evaluation: **AIC (Akaike Information Criterion)**

---

## Dashboard Features (Frontend)
 **Navigation Sidebar**: Switch between pages
 **Header**: Displays project title
 **Summary Section**: Shows **latest oil price, max/min prices**
 **Charts**:
   - **Line Chart**: Historical Brent oil price trend
   - **Volatility Chart**: Forecasted volatility from GARCH

---

