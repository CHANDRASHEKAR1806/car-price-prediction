# 🏎️ AutoDriven AI — Automobile Market Segmentation & Price Prediction Platform

[![Live App](https://img.shields.io/badge/Live_App-Streamlit_Cloud-00f2fe?style=for-the-badge&logo=streamlit)](https://car-price-ai06.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.13+-ff007f?style=for-the-badge&logo=python)](https://python.org)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.8.0-34d399?style=for-the-badge&logo=scikit-learn)](https://scikit-learn.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.46.1-FF4B4B?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![Plotly](https://img.shields.io/badge/Plotly-6.9.0-3f51b5?style=for-the-badge&logo=plotly)](https://plotly.com)

> An enterprise-grade, machine learning web application for **Automobile Price Valuation**, **Customer Market Clustering**, **Model Benchmark Diagnostics**, and **Side-by-Side Vehicle Analytics**.

---

## 🌐 Live Web Application

🚀 **Access the deployed live application here**:  
### **[https://car-price-ai06.streamlit.app](https://car-price-ai06.streamlit.app)**

---

## 🌟 Key Platform Modules & Features

### 1. 💰 AI-Powered Vehicle Price Predictor
- Predicts vehicle MSRP using a trained **Gradient Boosting Regressor** achieving **95.83% R² accuracy**.
- Features 1-click preset sample configurations (BMW M3 Performance, Toyota Camry, Ford F-150 Pickup).
- Generates **±6% Valuation Confidence Intervals**, **5-Year Projected Depreciation Curves**, and **Annual Fuel Expense Estimators**.

### 2. 📊 Customer Market Segmentation Engine
- Clusters 11,900+ vehicle records into 3 distinct buyer personas using **K-Means Unsupervised Learning**:
  - 🔵 **Cluster 0**: *Economy Commuters* (Avg Price $23k, 170 HP, 33 MPG)
  - 🟢 **Cluster 1**: *Mid-Range Family* (Avg Price $39k, 290 HP, 23 MPG)
  - 🟣 **Cluster 2**: *Luxury Sports & Exotics* (Avg Price $219k, 545 HP, 19 MPG)
- Interactive 3D Plotly spatial distribution maps and a **Live Vehicle Segment Classifier**.

### 3. 📈 Machine Learning Benchmark Suite
- Comparative evaluation dashboard analyzing **Linear Regression (62.01%)**, **Random Forest (97.29%)**, and **Gradient Boosting (95.83%)**.
- Interactive Feature Importance driver analysis and **Actual vs. Predicted scatter plots** with OLS trendlines.

### 4. 🏎️ Market Data Analytics & EDA
- Filter the dataset dynamically by Brand, Vehicle Body Style, and MSRP Range.
- View price distribution histograms, horsepower vs. price scatter plots, brand price rankings, and **Feature Correlation Heatmaps**.

### 5. ⚖️ Side-by-Side Vehicle Comparison Matrix
- Configure two vehicles simultaneously (Vehicle A vs. Vehicle B) to calculate instant MSRP valuation deltas, power-to-weight metrics, and comparative bar charts.

---

## 🎨 Design System & Architecture

- **Theme**: Cyberpunk Neon Dark Glassmorphism with glowing cyan/pink accents.
- **Fail-Safe Model Loader**: Features an automatic on-the-fly model fallback loader ensuring **0% crash probability** across all Python/OS environments.

```
Car_Price_Prediction_Project/
├── Dashboard.py                  # Main Landing Dashboard
├── style_utils.py               # Shared CSS Design Tokens & Cyberpunk Theme
├── pages/
│   ├── 1_Price_Prediction.py    # Price Predictor & Depreciation Engine
│   ├── 2_Market_Segmentation.py # K-Means 3D Clustering & Segment Classifier
│   ├── 3_Model_performace.py    # Model Benchmark Suite & Diagnostics
│   ├── 4_About_Project.py       # Architecture & Technology Overview
│   ├── 5_Market_Analytics.py    # Market Data Explorer & EDA Heatmaps
│   └── 6_Vehicle_Comparison.py  # Dual-Vehicle Comparison Matrix
├── assets/                       # Photorealistic Vehicle Showcase Gallery
├── data.csv                      # Automobile Dataset (11,914 vehicles)
├── car_price_gradient_boosting.pkl
├── car_segmentation_kmeans.pkl
├── clustering_scaler.pkl
└── requirements.txt             # Python Dependencies
```

---

## 🛠️ Local Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/CHANDRASHEKAR1806/car-price-prediction.git
   cd car-price-prediction
   ```

2. **Create a Virtual Environment & Install Dependencies**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Application**:
   ```bash
   streamlit run Dashboard.py
   ```

---

## 📊 Model Performance Summary

| Algorithm | R² Score | MAE | Status |
| :--- | :---: | :---: | :---: |
| **Linear Regression** | `0.6201` | Baseline | Evaluated |
| **Random Forest Regressor** | `0.9729` | High Fit | Evaluated |
| **Gradient Boosting Regressor** | `0.9583` | Production | **Selected Core Model** |

---

## 👨‍💻 Developer & Author

**Chandrashekar Jadhav**  
*Automobile Market Segmentation & Price Prediction Project*  
GitHub: [@CHANDRASHEKAR1806](https://github.com/CHANDRASHEKAR1806)  
Live Platform: [https://car-price-ai06.streamlit.app](https://car-price-ai06.streamlit.app)

---

© 2026 AutoDriven AI Platform. All rights reserved.
