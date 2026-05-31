import streamlit as st

st.set_page_config(
    page_title="Automobile Market Segmentation & Price Prediction",
    page_icon="🚗",
    layout="wide"
)
st.markdown("""
<style>

/* Sidebar background */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0f172a 0%,
        #1e293b 50%,
        #2563eb 100%
    );
}

/* Sidebar width */
section[data-testid="stSidebar"] {
    width: 320px !important;
}

/* Navigation buttons */
[data-testid="stSidebarNav"] {
    padding-top: 20px;
}

[data-testid="stSidebarNav"] a {
    border-radius: 12px;
    margin-bottom: 8px;
    padding: 10px;
}

[data-testid="stSidebarNav"] a:hover {
    background-color: rgba(59,130,246,0.3);
    border-left: 4px solid #60a5fa;
}

/* Selected page */
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: linear-gradient(90deg,#2563eb,#3b82f6);
    border-radius: 12px;
    color: white !important;
    font-weight: bold;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)
# =========================
# SIDEBAR
# =========================


# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main{
    padding-top:1rem;
}

.metric-card{
    background:#172554;
    padding:25px;
    border-radius:18px;
    text-align:center;
    color:white;
    box-shadow:0px 5px 15px rgba(0,0,0,.3);
}

.module-card{
    background:#0f172a;
    padding:25px;
    border-radius:18px;
    border:1px solid #334155;
    margin-bottom:15px;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# =========================
# WELCOME SECTION
# =========================

st.markdown("""
<h1 style='font-size:55px'>
🚗 Autodriven
</h1>

<h3 style='color:#3b82f6'>
AI Vehicle Intelligence Platform
</h3>
""", unsafe_allow_html=True) 
# =========================
# HERO SECTION
# =========================

st.markdown("""
<div style="
background:linear-gradient(135deg,#2563eb,#4f46e5);
padding:40px;
border-radius:20px;
color:white;
margin-bottom:30px;
">

<h1>🚗 Automobile Market Segmentation & Price Prediction</h1>

<h3>AI Powered Vehicle Analytics Platform</h3>

<p>
Predict vehicle prices, analyze market segments,
compare machine learning models and generate business insights.
</p>

</div>
""", unsafe_allow_html=True)



# =========================
# PROJECT OVERVIEW
# =========================

st.subheader("📋 Project Overview")

st.write("""
✅ Automobile Price Prediction

✅ Customer Market Segmentation

✅ Machine Learning Model Comparison

✅ Data Visualization & Analytics

✅ Business Intelligence Dashboard

✅ Performance Evaluation
""")

st.markdown("---")

# =========================
# PROJECT STATISTICS
# =========================

st.subheader("📊 Project Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>Dataset Size</h3>
        <h1>11,914</h1>
        <p>Cars</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>Best Model</h3>
        <h1>GBM</h1>
        <p>Gradient Boosting</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>R² Score</h3>
        <h1>95.83%</h1>
        <p>Prediction Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>Segments</h3>
        <h1>3</h1>
        <p>Customer Clusters</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# PROJECT MODULES
# =========================

st.subheader("🚀 Project Modules")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="module-card">
    <h3>💰 Price Prediction</h3>
    Predict vehicle prices using the trained Gradient Boosting Model.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="module-card">
    <h3>📊 Market Segmentation</h3>
    Analyze automobile market clusters using K-Means Clustering.
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="module-card">
    <h3>📈 Model Performance</h3>
    Compare Linear Regression, Random Forest and Gradient Boosting.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="module-card">
    <h3>📚 About Project</h3>
    View methodology, implementation details and project insights.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =========================
# QUICK INSIGHTS
# =========================

st.subheader("📌 Quick Insights")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("🚗 11,914 automobile records analyzed")

with col2:
    st.info("🎯 95.83% prediction accuracy achieved")

with col3:
    st.info("📊 3 customer market segments identified")

st.markdown("---")

# =========================
# FOOTER
# =========================

st.success("🎯 Use the navigation menu on the left to explore all project modules.")

st.markdown("---")

st.markdown("""
<center>

<h4>🚗 AutoDriven</h4>

Strategic Automobile Analytics Platform

Developed using Streamlit, Machine Learning,
K-Means Clustering and Gradient Boosting.

<br>

© 2026 Automobile Market Segmentation & Price Prediction Project

</center>
""", unsafe_allow_html=True)
