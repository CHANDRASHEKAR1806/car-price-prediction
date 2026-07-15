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
# ENCODING MAPS
# =====================================================
# IMPORTANT: These values must exactly match the sklearn LabelEncoder
# codes the model was TRAINED with (see MLEPROJECT_FINAL.ipynb, Section 4).
# LabelEncoder assigns codes alphabetically across ALL categories present
# in the full training dataset, not just the ones shown in this dropdown.
# The previous version of this file used made-up numbers here, which is
# why different cars were producing the same/near-identical price.
make_map = {
    "Acura": 0, "Alfa Romeo": 1, "Aston Martin": 2, "Audi": 3, "BMW": 4,
    "Bentley": 5, "Bugatti": 6, "Buick": 7, "Cadillac": 8, "Chevrolet": 9,
    "Chrysler": 10, "Dodge": 11, "FIAT": 12, "Ferrari": 13, "Ford": 14,
    "GMC": 15, "Genesis": 16, "HUMMER": 17, "Honda": 18, "Hyundai": 19,
    "Infiniti": 20, "Kia": 21, "Lamborghini": 22, "Land Rover": 23,
    "Lexus": 24, "Lincoln": 25, "Lotus": 26, "Maserati": 27, "Maybach": 28,
    "Mazda": 29, "McLaren": 30, "Mercedes-Benz": 31, "Mitsubishi": 32,
    "Nissan": 33, "Oldsmobile": 34, "Plymouth": 35, "Pontiac": 36,
    "Porsche": 37, "Rolls-Royce": 38, "Saab": 39, "Scion": 40, "Spyker": 41,
    "Subaru": 42, "Suzuki": 43, "Tesla": 44, "Toyota": 45, "Volkswagen": 46,
    "Volvo": 47
}

fuel_map = {
    "Diesel": 0,
    "Electric": 1,
    "Flex-fuel (premium unleaded recommended/E85)": 2,
    "Flex-fuel (premium unleaded required/E85)": 3,
    "Flex-fuel (unleaded/E85)": 4,
    "Flex-fuel (unleaded/natural gas)": 5,
    "Natural Gas": 6,
    "Premium Unleaded (recommended)": 7,
    "Premium Unleaded (required)": 8,
    "Regular Unleaded": 9
}

trans_map = {
    "Automated Manual": 0,
    "Automatic": 1,
    "Direct Drive": 2,
    "Manual": 3
}

drive_map = {
    "All Wheel Drive": 0,
    "Four Wheel Drive": 1,
    "Front Wheel Drive": 2,
    "Rear Wheel Drive": 3
}

size_map = {
    "Compact": 0,
    "Large": 1,
    "Midsize": 2
}

style_map = {
    "2dr Hatchback": 0, "2dr SUV": 1, "4dr Hatchback": 2, "4dr SUV": 3,
    "Cargo Minivan": 4, "Cargo Van": 5, "Convertible": 6,
    "Convertible SUV": 7, "Coupe": 8, "Crew Cab Pickup": 9,
    "Extended Cab Pickup": 10, "Passenger Minivan": 11, "Passenger Van": 12,
    "Regular Cab Pickup": 13, "Sedan": 14, "Wagon": 15
}

# =====================================================
# DROPDOWNS
# =====================================================
make_enc = st.selectbox("Car Brand", list(make_map.keys()), index=list(make_map.keys()).index("BMW"))
fuel_enc = st.selectbox("Fuel Type", list(fuel_map.keys()), index=list(fuel_map.keys()).index("Premium Unleaded (required)"))
trans_enc = st.selectbox("Transmission", list(trans_map.keys()), index=list(trans_map.keys()).index("Manual"))
drive_enc = st.selectbox("Drive Type", list(drive_map.keys()), index=list(drive_map.keys()).index("Rear Wheel Drive"))
size_enc = st.selectbox("Vehicle Size", list(size_map.keys()))
style_enc = st.selectbox("Vehicle Style", list(style_map.keys()), index=list(style_map.keys()).index("Coupe"))

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