import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
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

st.title("ℹ️ About Project")

st.markdown("""
<div style='background: linear-gradient(90deg,#0f172a,#2563eb);
padding:25px;
border-radius:15px;'>

<h2 style='color:white;text-align:center;'>
Strategic Automobile Market Segmentation & Price Prediction
</h2>

<p style='color:white;text-align:center;'>
Machine Learning Based Automobile Analytics Platform
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.header("🎯 Project Objective")

st.write("""
The objective of this project is to analyze automobile market data,
segment customers using K-Means Clustering, and predict vehicle prices
using Machine Learning algorithms.
""")

st.markdown("---")

st.header("🛠 Technologies Used")

st.write("""
• Python

• Streamlit

• Pandas

• NumPy

• Scikit-Learn

• Matplotlib

• Joblib
""")

st.markdown("---")

st.header("🤖 Machine Learning Models")

st.write("""
• Linear Regression

• Random Forest Regressor

• Gradient Boosting Regressor

• K-Means Clustering
""")

st.markdown("---")

st.header("📊 Dataset Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Dataset Size", "11,914 Cars")

with col2:
    st.metric("Features", "16")

st.markdown("---")

st.header("🏆 Final Results")

st.success("""
Best Prediction Model:
Gradient Boosting Regressor

R² Score: 0.9583
""")

st.markdown("---")

st.header("👨‍💻 Developer")

st.info("""
Chandrashekar Jadhav

Automobile Market Segmentation & Price Prediction Project

2026
""")

st.markdown("---")

st.markdown("""
<center>
<h3>🚘 AutoDriven</h3>
<p>Strategic Automobile Analytics Platform</p>
<p>© 2026 All Rights Reserved</p>
</center>
""", unsafe_allow_html=True)
