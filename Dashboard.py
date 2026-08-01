import streamlit as st
import pandas as pd
from pathlib import Path
from style_utils import apply_custom_styles, render_header, render_footer, get_asset_image

# ==========================================
# PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="AutoDriven | Automobile Intelligence Platform",
    page_icon="🚗",
    layout="wide"
)

# Apply global dark glassmorphism design system & top-left branding
apply_custom_styles()

# ==========================================
# HERO HEADER
# ==========================================
render_header(
    title="AutoDriven AI Platform",
    subtitle="Strategic Automobile Market Analytics, Customer Segmentation & Precision Price Prediction Engine",
    icon="🏎️",
    tag="Cyberpunk AI Engine 2026"
)

# ==========================================
# HERO SHOWCASE WITH REAL CAR IMAGE
# ==========================================
sports_img = get_asset_image("luxury_sports")
sedan_img = get_asset_image("family_sedan")
suv_img = get_asset_image("suv_pickup")

hero_col1, hero_col2 = st.columns([1.3, 1])

with hero_col1:
    st.markdown("""
    <div class="glass-card" style="border-color: rgba(0, 242, 254, 0.4);">
        <span class="badge badge-blue">ENTERPRISE INTELLIGENCE</span>
        <h2 style="font-family: Outfit; font-weight: 800; color: white; margin-top: 10px;">AI-Driven Automobile Market Analytics</h2>
        <p style="color: #cbd5e1; font-size: 1.05rem; line-height: 1.7;">
            Welcome to <strong>AutoDriven AI</strong> — the next-generation machine learning platform built for vehicle price prediction, customer market cluster analysis, and real-time comparative valuation.
        </p>
        <div style="display: flex; gap: 15px; margin-top: 15px;">
            <span style="color: #00f2fe; font-weight: 700;">✓ 11,914 Verified Vehicles</span>
            <span style="color: #34d399; font-weight: 700;">✓ 95.83% Model Accuracy</span>
            <span style="color: #ff007f; font-weight: 700;">✓ 3 Market Clusters</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with hero_col2:
    if sports_img:
        st.image(sports_img, caption="🏎️ High-Performance Luxury Sports Valuation Class", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# EXECUTIVE SUMMARY STATS
# ==========================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card-pro">
        <div class="metric-label">Dataset Vehicles</div>
        <div class="metric-val">11,914</div>
        <div class="metric-sub">Across 48 Top Brands</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card-pro">
        <div class="metric-label">Best Model R²</div>
        <div class="metric-val">95.83%</div>
        <div class="metric-sub">Gradient Boosting Regressor</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card-pro">
        <div class="metric-label">Customer Segments</div>
        <div class="metric-val">3 Clusters</div>
        <div class="metric-sub">K-Means Algorithmic Model</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card-pro">
        <div class="metric-label">Features Tracked</div>
        <div class="metric-val">16 Key Specs</div>
        <div class="metric-sub">HP, MPG, Size, Style & Brand</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# PLATFORM MODULES SHOWCASE WITH REAL CAR IMAGES
# ==========================================
st.markdown("<h2 style='font-family: Outfit; font-weight: 700; color: white;'>🚀 Core Platform Modules</h2>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <h3 style="color: #00f2fe; margin: 0; font-family: Outfit; font-weight: 700;">💰 Vehicle Price Predictor</h3>
            <span class="badge badge-blue">Regression ML</span>
        </div>
        <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
            Leverage our trained <strong>Gradient Boosting model</strong> to estimate exact vehicle valuation based on engine specs, horsepower, fuel type, body style, and manufacture year.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if sedan_img:
        st.image(sedan_img, caption="🚙 Executive Sedan & Family Commuter Price Valuation Engine", use_container_width=True)

with c2:
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px;">
            <h3 style="color: #34d399; margin: 0; font-family: Outfit; font-weight: 700;">📊 Customer Market Segmentation</h3>
            <span class="badge badge-green">K-Means AI</span>
        </div>
        <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6;">
            Explore vehicle market clusters (Economy Commuters, Mid-Range Family, Luxury Sports) using 3D interactive visualizations and classify any vehicle specs into buyer personas.
        </p>
    </div>
    """, unsafe_allow_html=True)
    if suv_img:
        st.image(suv_img, caption="🏔️ Luxury SUV & All-Terrain Market Cluster Classification", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# LIVE DATASET EXPLORER SNIPPET
# ==========================================
st.markdown("<h2 style='font-family: Outfit; font-weight: 700; color: white;'>🔍 Dataset Quick Explorer</h2>", unsafe_allow_html=True)

BASE_DIR = Path(__file__).parent
data_path = BASE_DIR / "data.csv"

if data_path.exists():
    @st.cache_data
    def load_data():
        df = pd.read_csv(data_path)
        return df

    df = load_data()
    
    col_filter1, col_filter2 = st.columns([1, 3])
    with col_filter1:
        selected_make = st.selectbox("Filter Brand", ["All Makes"] + sorted(df["Make"].dropna().unique().tolist()))
    with col_filter2:
        search_query = st.text_input("Search Vehicle Model", placeholder="e.g. M3, Camry, Mustang, Civic...")

    filtered_df = df.copy()
    if selected_make != "All Makes":
        filtered_df = filtered_df[filtered_df["Make"] == selected_make]
    if search_query:
        filtered_df = filtered_df[filtered_df["Model"].astype(str).str.contains(search_query, case=False, na=False)]

    st.markdown(f"<span style='color: #94a3b8; font-size: 0.9rem;'>Showing <strong>{len(filtered_df):,}</strong> matching records out of {len(df):,} total</span>", unsafe_allow_html=True)
    st.dataframe(
        filtered_df[["Make", "Model", "Year", "Engine HP", "Engine Cylinders", "Transmission Type", "Driven_Wheels", "highway MPG", "city mpg", "MSRP"]].head(10),
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================
render_footer()
