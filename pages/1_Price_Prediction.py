import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    
    page_title="Automobile Price Prediction",
    page_icon="🚘",
    layout="wide"
)
st.markdown("""
<style>

/* Sidebar Background */
section[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #081028 0%,
        #12213f 50%,
        #2563eb 100%
    );
}

/* Sidebar Text */
section[data-testid="stSidebar"] *{
    color: white;
}

/* Navigation Items */
[data-testid="stSidebarNav"] a{
    border-radius: 15px;
    margin-bottom: 10px;
    padding: 10px;
    transition: 0.3s;
}

/* Active Page */
[data-testid="stSidebarNav"] a[aria-current="page"]{
    background: linear-gradient(
        90deg,
        #2563eb,
        #60a5fa
    );
    font-weight: bold;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

/* Hover Effect */
[data-testid="stSidebarNav"] a:hover{
    background: rgba(255,255,255,0.15);
    border-radius: 15px;
}

/* Remove Extra Top Space */
[data-testid="stSidebarNav"]{
    padding-top: 10px;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")

# =====================================================
# LOAD MODEL
# =====================================================
BASE_DIR = Path(__file__).parent.parent

model = joblib.load(BASE_DIR / "car_price_gradient_boosting.pkl")

# =====================================================
# SIDEBAR
# =====================================================


# =====================================================
# HEADER
# =====================================================
st.title("🚘 Automobile Price Prediction")

st.markdown("""
<div style='background: linear-gradient(90deg,#0f172a,#2563eb);
padding:35px;
border-radius:20px;
box-shadow:0 0 15px rgba(0,0,0,0.3);'>

<h1 style='color:white;text-align:center;'>
🚘 AI Powered Car Price Prediction System
</h1>

<p style='color:white;text-align:center;font-size:20px;'>
Predict vehicle prices using Machine Learning and Gradient Boosting Regression
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# MODEL PERFORMANCE
# =====================================================
st.markdown("---")

st.subheader("📊 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Linear Regression", "0.6201")

with col2:
    st.metric("Random Forest", "0.9729")

with col3:
    st.metric("Gradient Boosting", "0.9583")

st.success("🏆 Selected Model: Gradient Boosting")

# =====================================================
# INPUT SECTION
# =====================================================
st.markdown("---")

st.subheader("💰 Vehicle Price Prediction")

with col1:
    engine_hp = st.number_input("Engine HP", value=200.0)
    highway_mpg = st.number_input("Highway MPG", value=25.0)
    city_mpg = st.number_input("City MPG", value=18.0)
    engine_cylinders = st.number_input("Engine Cylinders", value=4.0)

with col2:
    num_doors = st.number_input("Number of Doors", value=4.0)
    year = st.number_input("Year", value=2020)
    popularity = st.number_input("Popularity", value=1500)

# =====================================================
# DROPDOWNS
# =====================================================
make_enc = st.selectbox(
    "Car Brand",
    ["BMW", "Audi", "Toyota", "Honda", "Ford"]
)

fuel_enc = st.selectbox(
    "Fuel Type",
    ["Premium", "Regular", "Diesel"]
)

trans_enc = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

drive_enc = st.selectbox(
    "Drive Type",
    ["Rear Wheel Drive", "Front Wheel Drive", "All Wheel Drive"]
)

size_enc = st.selectbox(
    "Vehicle Size",
    ["Compact", "Midsize", "Large"]
)

style_enc = st.selectbox(
    "Vehicle Style",
    ["Coupe", "Sedan", "SUV", "Convertible"]
)

# =====================================================
# ENCODING MAPS
# =====================================================
make_map = {
    "BMW": 7,
    "Audi": 1,
    "Toyota": 2,
    "Honda": 3,
    "Ford": 4
}

fuel_map = {
    "Premium": 3,
    "Regular": 1,
    "Diesel": 2
}

trans_map = {
    "Manual": 4,
    "Automatic": 0
}

drive_map = {
    "Rear Wheel Drive": 2,
    "Front Wheel Drive": 1,
    "All Wheel Drive": 0
}

size_map = {
    "Compact": 0,
    "Midsize": 1,
    "Large": 2
}

style_map = {
    "Coupe": 2,
    "Sedan": 3,
    "SUV": 4,
    "Convertible": 1
}

# =====================================================
# PREDICTION
# =====================================================
# =====================================================
# BUTTONS
# =====================================================

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    predict_btn = st.button(
        "🚀 Predict Price",
        use_container_width=True
    )

with col_btn2:
    reset_btn = st.button(
        "🔄 Clear Inputs",
        use_container_width=True
    )

if reset_btn:
    st.rerun()

# =====================================================
# PREDICTION
# =====================================================

if predict_btn:

    features = np.array([[
        engine_hp,
        highway_mpg,
        city_mpg,
        engine_cylinders,
        num_doors,
        year,
        popularity,
        make_map[make_enc],
        fuel_map[fuel_enc],
        trans_map[trans_enc],
        drive_map[drive_enc],
        size_map[size_enc],
        style_map[style_enc]
    ]])

    prediction = model.predict(features)

    st.markdown(f"""
    <div style="
    background: linear-gradient(90deg,#0f5132,#198754);
    padding:25px;
    border-radius:15px;
    text-align:center;
    margin-top:20px;
    ">

    <h2 style="color:white;">
    💰 Predicted Vehicle Price
    </h2>

    <h1 style="color:#90EE90;">
    ₹ {prediction[0]:,.2f}
    </h1>

    </div>
    """, unsafe_allow_html=True)
# =====================================================
# PREDICTION SUMMARY
# =====================================================
st.markdown("---")

st.markdown("""
<div style="
background: linear-gradient(90deg,#0f172a,#1e3a8a);
padding:20px;
border-radius:15px;
margin-top:20px;
">

<h3 style="color:white;text-align:center;">
🚘 Intelligent Vehicle Price Estimation
</h3>

<p style="color:white;text-align:center;">
This AI system predicts vehicle prices using a trained Gradient Boosting
Machine Learning model with an accuracy of 95.83%.
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")

st.markdown("""
<div style='text-align:center'>

<h3>🛞 AutoDriven</h3>

<p>
Strategic Automobile Market Segmentation & Price Prediction
</p>

<p>
Developed by Chandrashekar Jadhav
</p>

<p>
© 2026 All Rights Reserved
</p>

</div>
""", unsafe_allow_html=True)
