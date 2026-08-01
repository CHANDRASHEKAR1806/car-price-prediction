import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from style_utils import apply_custom_styles, render_header, render_footer, get_asset_image

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Market Segmentation | AutoDriven",
    page_icon="📊",
    layout="wide"
)

apply_custom_styles()

BASE_DIR = Path(__file__).parent.parent
kmeans_model = joblib.load(BASE_DIR / "car_segmentation_kmeans.pkl")
scaler = joblib.load(BASE_DIR / "clustering_scaler.pkl")

# Real car images
sports_img = get_asset_image("luxury_sports")
sedan_img = get_asset_image("family_sedan")
suv_img = get_asset_image("suv_pickup")

# Load data
csv_path = BASE_DIR / "car segmentation data.csv"
if not csv_path.exists():
    csv_path = BASE_DIR / "data.csv"

@st.cache_data
def load_cluster_data(path):
    df = pd.read_csv(path)
    return df

df_seg = load_cluster_data(csv_path)

# Correct feature ordering matching scaler.fit: ['MSRP', 'Engine HP', 'highway MPG']
if "Cluster" not in df_seg.columns and "Engine HP" in df_seg.columns:
    cluster_features = df_seg[["MSRP", "Engine HP", "highway MPG"]].dropna()
    scaled_feats = scaler.transform(cluster_features)
    df_seg.loc[cluster_features.index, "Cluster"] = kmeans_model.predict(scaled_feats)

cluster_names = {
    0: "Economy Commuters",
    1: "Mid-Range Family",
    2: "Luxury Sports"
}

if "Cluster" in df_seg.columns:
    df_seg["Segment Name"] = df_seg["Cluster"].map(cluster_names).fillna("Unassigned")

# =====================================================
# HEADER
# =====================================================
render_header(
    title="Customer Market Segmentation",
    subtitle="Algorithmic Customer Clustering & Vehicle Segmentation using K-Means Unsupervised Learning",
    icon="📊",
    tag="K-Means Clustering Engine"
)

# =====================================================
# SEGMENT CARDS OVERVIEW WITH REAL CAR IMAGES
# =====================================================
st.markdown("<h2 style='font-family: Outfit; font-weight: 700; color: white;'>🚗 Identified Market Segments</h2>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    if sedan_img:
        st.image(sedan_img, use_container_width=True)
    st.markdown("""
    <div class="glass-card">
        <span class="badge badge-blue">Cluster 0</span>
        <h3 style="color: #00f2fe; font-family: Outfit; margin: 10px 0 5px 0;">Economy Commuters</h3>
        <p style="color: #94a3b8; font-size: 0.9rem;">Fuel efficient, practical daily vehicles aimed at mass budget buyers.</p>
        <hr style="border-color: rgba(255,255,255,0.1);">
        <p style="color: #cbd5e1; margin: 4px 0;">💰 Avg Price: <strong>$23,565</strong></p>
        <p style="color: #cbd5e1; margin: 4px 0;">⚙️ Avg Horsepower: <strong>170 HP</strong></p>
        <p style="color: #cbd5e1; margin: 4px 0;">⛽ Highway Efficiency: <strong>33 MPG</strong></p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    if suv_img:
        st.image(suv_img, use_container_width=True)
    st.markdown("""
    <div class="glass-card">
        <span class="badge badge-green">Cluster 1</span>
        <h3 style="color: #34d399; font-family: Outfit; margin: 10px 0 5px 0;">Mid-Range Family</h3>
        <p style="color: #94a3b8; font-size: 0.9rem;">Balanced performance, luxury comfort, and family utility.</p>
        <hr style="border-color: rgba(255,255,255,0.1);">
        <p style="color: #cbd5e1; margin: 4px 0;">💰 Avg Price: <strong>$39,171</strong></p>
        <p style="color: #cbd5e1; margin: 4px 0;">⚙️ Avg Horsepower: <strong>290 HP</strong></p>
        <p style="color: #cbd5e1; margin: 4px 0;">⛽ Highway Efficiency: <strong>23 MPG</strong></p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    if sports_img:
        st.image(sports_img, use_container_width=True)
    st.markdown("""
    <div class="glass-card">
        <span class="badge badge-purple">Cluster 2</span>
        <h3 style="color: #ff007f; font-family: Outfit; margin: 10px 0 5px 0;">Luxury Sports & Exotics</h3>
        <p style="color: #94a3b8; font-size: 0.9rem;">High performance supercars, luxury sedans, and exotic hypercars.</p>
        <hr style="border-color: rgba(255,255,255,0.1);">
        <p style="color: #cbd5e1; margin: 4px 0;">💰 Avg Price: <strong>$219,890</strong></p>
        <p style="color: #cbd5e1; margin: 4px 0;">⚙️ Avg Horsepower: <strong>545 HP</strong></p>
        <p style="color: #cbd5e1; margin: 4px 0;">⛽ Highway Efficiency: <strong>19 MPG</strong></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# INTERACTIVE 3D CLUSTER MAP
# =====================================================
st.markdown("<h2 style='font-family: Outfit; font-weight: 700; color: white;'>📈 Interactive 3D Market Cluster Space</h2>", unsafe_allow_html=True)

if "Cluster" in df_seg.columns and "Engine HP" in df_seg.columns:
    sample_df = df_seg.dropna(subset=["Engine HP", "MSRP", "highway MPG", "Segment Name"]).sample(min(1500, len(df_seg)), random_state=42)

    fig_3d = px.scatter_3d(
        sample_df,
        x="Engine HP",
        y="highway MPG",
        z="MSRP",
        color="Segment Name",
        hover_data=["Make", "Model", "Year"],
        title="3D Spatial Distribution: Horsepower vs MPG vs Price",
        color_discrete_map={
            "Economy Commuters": "#00f2fe",
            "Mid-Range Family": "#10b981",
            "Luxury Sports": "#ff007f"
        },
        opacity=0.85
    )

    fig_3d.update_layout(
        paper_bgcolor="rgba(15, 23, 42, 0.6)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        font_color="#f8fafc",
        height=550,
        margin=dict(l=10, r=10, t=40, b=10)
    )

    st.plotly_chart(fig_3d, use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# LIVE CUSTOMER SEGMENT CLASSIFIER WIDGET
# =====================================================
st.markdown("<h2 style='font-family: Outfit; font-weight: 700; color: white;'>🎯 Live Vehicle Segment Classifier</h2>", unsafe_allow_html=True)
st.markdown("<p style='color: #cbd5e1;'>Input vehicle parameters below to determine which customer segment it belongs to:</p>", unsafe_allow_html=True)

col_in1, col_in2, col_in3 = st.columns(3)

with col_in1:
    test_price = st.number_input("Estimated Price MSRP ($)", value=35000.0, step=1000.0)
with col_in2:
    test_hp = st.number_input("Horsepower (HP)", value=250.0, step=10.0)
with col_in3:
    test_mpg = st.number_input("Highway Fuel Efficiency (MPG)", value=28.0, step=1.0)

if st.button("🔍 Classify Vehicle Market Segment", type="primary", use_container_width=True):
    # Order matching scaler fit: MSRP, Engine HP, highway MPG
    scaled_input = scaler.transform([[test_price, test_hp, test_mpg]])
    cluster_pred = kmeans_model.predict(scaled_input)[0]
    seg_title = cluster_names.get(cluster_pred, "Unknown")

    if cluster_pred == 0:
        badge_cls = "badge-blue"
    elif cluster_pred == 1:
        badge_cls = "badge-green"
    else:
        badge_cls = "badge-purple"

    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(20, 8, 40, 0.9) 0%, rgba(8, 2, 18, 0.95) 100%);
        border: 1px solid rgba(0, 242, 254, 0.4);
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        margin-top: 20px;
    ">
        <span class="badge {badge_cls}" style="font-size: 0.9rem;">Assigned Cluster {cluster_pred}</span>
        <h2 style="color: white; font-family: Outfit; margin-top: 10px;">Classification Result: <span style="color: #00f2fe;">{seg_title}</span></h2>
        <p style="color: #cbd5e1; max-width: 600px; margin: 0 auto;">
            This vehicle targets buyers in the <strong>{seg_title}</strong> demographic based on its price point (${test_price:,.0f}), power ({test_hp} HP), and efficiency ({test_mpg} MPG).
        </p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================
render_footer()
