import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from style_utils import apply_custom_styles, render_header, render_footer

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Market Analytics | AutoDriven",
    page_icon="🏎️",
    layout="wide"
)

apply_custom_styles()

BASE_DIR = Path(__file__).parent.parent
data_path = BASE_DIR / "data.csv"

@st.cache_data
def load_data():
    return pd.read_csv(data_path)

df = load_data()

# =====================================================
# HEADER
# =====================================================
render_header(
    title="Market Data Analytics & Exploratory Data Analysis",
    subtitle="Deep data exploration, correlation insights, and price distribution analytics across 11,900+ vehicle records",
    icon="🏎️",
    tag="Exploratory Data Analysis"
)

# =====================================================
# FILTER CONTROLS
# =====================================================
st.markdown("<h3 style='font-family: Outfit; color: white;'>🔍 Dataset Filters</h3>", unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns(3)

with col_f1:
    makes = ["All Makes"] + sorted(df["Make"].dropna().unique().tolist())
    sel_make = st.selectbox("Select Brand", makes)

with col_f2:
    styles = ["All Styles"] + sorted(df["Vehicle Style"].dropna().unique().tolist())
    sel_style = st.selectbox("Select Vehicle Style", styles)

with col_f3:
    max_price_slider = float(df["MSRP"].max())
    price_range = st.slider("Price MSRP Range ($)", 0.0, 500000.0, (0.0, 200000.0), step=5000.0)

# Filter dataset
df_filtered = df[(df["MSRP"] >= price_range[0]) & (df["MSRP"] <= price_range[1])]

if sel_make != "All Makes":
    df_filtered = df_filtered[df_filtered["Make"] == sel_make]

if sel_style != "All Styles":
    df_filtered = df_filtered[df_filtered["Vehicle Style"] == sel_style]

st.markdown(f"<span style='color: #94a3b8; font-size: 0.95rem;'>Filtered dataset contains <strong>{len(df_filtered):,}</strong> records</span>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# ANALYTICS DASHBOARD
# =====================================================
st.markdown("<h2 style='font-family: Outfit; font-weight: 700; color: white;'>📊 Market Distribution Charts</h2>", unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    # Price Distribution Histogram
    fig_hist = px.histogram(
        df_filtered,
        x="MSRP",
        nbins=40,
        title="Vehicle Price (MSRP) Distribution",
        color_discrete_sequence=["#3b82f6"],
        marginal="box"
    )
    fig_hist.update_layout(
        paper_bgcolor="rgba(15, 23, 42, 0.6)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        font_color="#f8fafc",
        height=380
    )
    st.plotly_chart(fig_hist, use_container_width=True)

with c2:
    # HP vs Price Scatter Plot
    fig_hp_price = px.scatter(
        df_filtered,
        x="Engine HP",
        y="MSRP",
        color="Transmission Type" if "Transmission Type" in df_filtered.columns else None,
        hover_data=["Make", "Model", "Year"],
        title="Horsepower (HP) vs Price (MSRP)",
        opacity=0.7
    )
    fig_hp_price.update_layout(
        paper_bgcolor="rgba(15, 23, 42, 0.6)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        font_color="#f8fafc",
        height=380
    )
    st.plotly_chart(fig_hp_price, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# TOP BRANDS & CORRELATION MATRIX
# =====================================================
c3, c4 = st.columns(2)

with c3:
    # Top 15 Brands by Avg Price
    brand_avg = df.groupby("Make")["MSRP"].mean().reset_index().sort_values("MSRP", ascending=False).head(15)
    fig_brand = px.bar(
        brand_avg,
        x="MSRP",
        y="Make",
        orientation="h",
        title="🏆 Top 15 Highest Average MSRP Car Brands",
        color="MSRP",
        color_continuous_scale="Viridis"
    )
    fig_brand.update_layout(
        paper_bgcolor="rgba(15, 23, 42, 0.6)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        font_color="#f8fafc",
        height=400,
        coloraxis_showscale=False
    )
    st.plotly_chart(fig_brand, use_container_width=True)

with c4:
    # Correlation Matrix
    num_cols = ["Engine HP", "Engine Cylinders", "highway MPG", "city mpg", "Popularity", "MSRP"]
    corr = df[num_cols].corr()

    fig_corr = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        title="🔥 Feature Correlation Heatmap",
        color_continuous_scale="RdBu_r"
    )
    fig_corr.update_layout(
        paper_bgcolor="rgba(15, 23, 42, 0.6)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        font_color="#f8fafc",
        height=400
    )
    st.plotly_chart(fig_corr, use_container_width=True)

# =====================================================
# FOOTER
# =====================================================
render_footer()
