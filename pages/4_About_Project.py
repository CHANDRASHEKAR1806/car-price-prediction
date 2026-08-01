import streamlit as st
from style_utils import apply_custom_styles, render_header, render_footer

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="About Project | AutoDriven",
    page_icon="ℹ️",
    layout="wide"
)

apply_custom_styles()

# =====================================================
# HEADER
# =====================================================
render_header(
    title="About AutoDriven AI Platform",
    subtitle="Enterprise Machine Learning Architecture for Automobile Pricing & Customer Market Segmentation",
    icon="ℹ️",
    tag="System Architecture"
)

# =====================================================
# OVERVIEW SECTIONS
# =====================================================
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #60a5fa; font-family: Outfit; margin-top: 0;">🎯 Objectives & Scope</h3>
        <p style="color: #cbd5e1; line-height: 1.7;">
            The <strong>AutoDriven Platform</strong> is built to empower automotive analysts, dealerships, and buyers with predictive market intelligence. It addresses two core challenges:
        </p>
        <ul style="color: #cbd5e1; line-height: 1.8;">
            <li><strong>Automobile Price Prediction:</strong> Accurately predicting market MSRP across 48 global brands using non-linear ensemble regression models.</li>
            <li><strong>Customer Market Segmentation:</strong> Uncovering distinct consumer buyer profiles (Economy Commuters, Mid-Range Family, Luxury Sports) using unsupervised K-Means clustering.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #34d399; font-family: Outfit; margin-top: 0;">🛠 Technology Stack</h3>
        <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 15px;">
            <span class="badge badge-blue">Python 3.13</span>
            <span class="badge badge-blue">Streamlit 1.46</span>
            <span class="badge badge-green">Scikit-Learn 1.7</span>
            <span class="badge badge-green">Pandas & NumPy</span>
            <span class="badge badge-purple">Plotly Express</span>
            <span class="badge badge-purple">Joblib Serialization</span>
            <span class="badge badge-amber">K-Means Clustering</span>
            <span class="badge badge-amber">Gradient Boosting</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# ARCHITECTURE PIPELINE
# =====================================================
st.markdown("<h2 style='font-family: Outfit; font-weight: 700; color: white;'>⚙️ Machine Learning Pipeline Architecture</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; text-align: center;">
        <div style="flex: 1; min-width: 180px;">
            <div style="font-size: 2rem;">📁 Data Ingestion</div>
            <p style="color: #94a3b8; font-size: 0.85rem;">11,914 Vehicle Records & 16 Features</p>
        </div>
        <div style="font-size: 1.5rem; color: #3b82f6;">➔</div>
        <div style="flex: 1; min-width: 180px;">
            <div style="font-size: 2rem;">🧹 Preprocessing</div>
            <p style="color: #94a3b8; font-size: 0.85rem;">Label Encoding & Standard Scaling</p>
        </div>
        <div style="font-size: 1.5rem; color: #3b82f6;">➔</div>
        <div style="flex: 1; min-width: 180px;">
            <div style="font-size: 2rem;">🤖 Training</div>
            <p style="color: #94a3b8; font-size: 0.85rem;">Gradient Boosting & K-Means</p>
        </div>
        <div style="font-size: 1.5rem; color: #3b82f6;">➔</div>
        <div style="flex: 1; min-width: 180px;">
            <div style="font-size: 2rem;">🚀 Deployment</div>
            <p style="color: #94a3b8; font-size: 0.85rem;">Streamlit Web Platform</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# DEVELOPER CREDITS
# =====================================================
st.markdown("""
<div class="glass-card" style="text-align: center; border-color: rgba(99, 102, 241, 0.4);">
    <h3 style="color: white; font-family: Outfit; margin-top: 0;">👨‍💻 Developer & Maintainer</h3>
    <h2 style="color: #60a5fa; font-family: Outfit; margin: 5px 0;">Chandrashekar Jadhav</h2>
    <p style="color: #94a3b8; font-size: 0.95rem;">Automobile Market Segmentation & Price Prediction Project • © 2026</p>
    <a href="https://github.com/CHANDRASHEKAR1806/car-price-prediction" target="_blank" style="
        display: inline-block;
        background: linear-gradient(135deg, #2563eb, #4f46e5);
        color: white;
        padding: 8px 20px;
        border-radius: 20px;
        text-decoration: none;
        font-weight: 600;
        font-size: 0.9rem;
        margin-top: 10px;
    ">
        🔗 View GitHub Repository
    </a>
</div>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================
render_footer()
