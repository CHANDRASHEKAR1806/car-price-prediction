import streamlit as st
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

def get_asset_image(keyword):
    """Finds image path in assets directory matching keyword."""
    assets_dir = BASE_DIR / "assets"
    if assets_dir.exists():
        for f in os.listdir(assets_dir):
            if keyword in f and f.endswith(".jpg"):
                return str(assets_dir / f)
    return None

def apply_custom_styles():
    """Injects top sidebar brand logo (ABOVE Dashboard) and Cyberpunk design tokens with zero gap."""
    
    # -------------------------------------------------------------
    # TOP-LEFT SIDEBAR BRAND LOGO CARD
    # -------------------------------------------------------------
    st.sidebar.markdown("""
    <div class="top-sidebar-brand-card">
        <div style="display: flex; align-items: center; gap: 14px;">
            <div style="
                font-size: 2rem;
                background: rgba(0, 242, 254, 0.15);
                padding: 8px 12px;
                border-radius: 14px;
                border: 1px solid rgba(0, 242, 254, 0.4);
                filter: drop-shadow(0 0 10px #00f2fe);
            ">🏎️</div>
            <div>
                <h2 style="
                    font-family: 'Outfit', sans-serif;
                    font-weight: 900;
                    color: #00f2fe;
                    margin: 0;
                    letter-spacing: 1px;
                    font-size: 1.45rem;
                    text-shadow: 0 0 12px rgba(0, 242, 254, 0.7);
                ">
                    AutoDriven
                </h2>
                <div style="
                    font-size: 0.72rem;
                    color: #ff007f;
                    font-weight: 800;
                    letter-spacing: 1.8px;
                    text-transform: uppercase;
                    margin-top: 4px;
                ">
                    AI VEHICLE INTELLIGENCE
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # GLOBAL CYBERPUNK CSS & ZERO-GAP FLEX RE-ORDERING
    # -------------------------------------------------------------
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800;900&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Global Cyberpunk Dark Background */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #1a0933 0%, #05020a 85%);
        color: #f8fafc;
    }

    /* Sidebar Container & Zero Gap Layout */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #090314 0%, #150528 50%, #06020c 100%) !important;
        border-right: 1px solid rgba(0, 242, 254, 0.25) !important;
        width: 320px !important;
    }

    section[data-testid="stSidebar"] > div:first-child {
        display: flex !important;
        flex-direction: column !important;
        padding-top: 0px !important;
    }

    /* MOVE CUSTOM SIDEBAR BRAND CARD TO VERY TOP WITH ZERO GAP BELOW */
    [data-testid="stSidebarUserContent"] {
        order: -1 !important;
        padding-top: 10px !important;
        padding-bottom: 0px !important;
        margin-bottom: 0px !important;
    }

    /* SIDEBAR NAV STARTS IMMEDIATELY BELOW BRAND CARD WITHOUT GAP */
    [data-testid="stSidebarNav"] {
        order: 1 !important;
        padding-top: 0px !important;
        margin-top: 0px !important;
    }

    [data-testid="stSidebarNav"] ul {
        padding-top: 0px !important;
        margin-top: 0px !important;
    }

    /* Brand Logo Card Styling at Top */
    .top-sidebar-brand-card {
        background: linear-gradient(135deg, rgba(20, 8, 40, 0.95) 0%, rgba(8, 2, 18, 0.98) 100%);
        border: 1px solid rgba(0, 242, 254, 0.4);
        border-radius: 20px;
        padding: 16px 18px;
        margin: 5px 10px 4px 10px !important; /* Minimal bottom margin to remove gap */
        box-shadow: 0 0 22px rgba(0, 242, 254, 0.3);
    }

    /* ULTRA-BRIGHT HIGH-CONTRAST SIDEBAR BUTTONS */
    [data-testid="stSidebarNav"] a {
        border-radius: 14px !important;
        margin: 5px 10px !important;
        padding: 14px 18px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(0, 242, 254, 0.25) !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4) !important;
    }

    [data-testid="stSidebarNav"] a span {
        color: #ffffff !important; /* Extremely Bright White Text */
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        text-shadow: 0 1px 3px rgba(0,0,0,0.8);
    }

    /* Hover Navigation Link */
    [data-testid="stSidebarNav"] a:hover {
        background: rgba(0, 242, 254, 0.25) !important;
        border-color: #00f2fe !important;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.6) !important;
        transform: translateX(6px) !important;
    }

    [data-testid="stSidebarNav"] a:hover span {
        color: #00f2fe !important;
        text-shadow: 0 0 10px rgba(0, 242, 254, 0.8);
    }

    /* Active Page Navigation Item - Glowing Neon Cyan with Dark Bold Text */
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%) !important;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.9) !important;
        border: 2px solid #ffffff !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] span {
        color: #030712 !important; /* Deep Black Text on Bright Neon Cyan */
        font-weight: 900 !important;
        font-size: 1.08rem !important;
        text-shadow: none !important;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(18, 8, 38, 0.75);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid rgba(0, 242, 254, 0.25);
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        transition: all 0.4s ease;
    }

    .glass-card:hover {
        border-color: #00f2fe;
        transform: translateY(-6px);
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.4);
    }

    /* Metric Cards */
    .metric-card-pro {
        background: linear-gradient(145deg, rgba(25, 10, 48, 0.85), rgba(10, 4, 20, 0.95));
        border: 1px solid rgba(0, 242, 254, 0.25);
        border-radius: 18px;
        padding: 22px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
        transition: all 0.3s ease;
    }

    .metric-card-pro:hover {
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.5);
        transform: scale(1.02);
    }

    .metric-card-pro::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #00f2fe, #ff007f);
    }

    .metric-val {
        font-family: 'Outfit', sans-serif;
        font-size: 2.3rem;
        font-weight: 800;
        color: #00f2fe;
        text-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
        margin: 6px 0;
    }

    .metric-label {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #cbd5e1;
        font-weight: 700;
    }

    .metric-sub {
        font-size: 0.8rem;
        color: #94a3b8;
    }

    /* Badges */
    .badge {
        display: inline-block;
        padding: 5px 14px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    .badge-blue {
        background: rgba(0, 242, 254, 0.2);
        color: #00f2fe;
        border: 1px solid rgba(0, 242, 254, 0.5);
    }

    .badge-green {
        background: rgba(16, 185, 129, 0.2);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.5);
    }

    .badge-purple {
        background: rgba(255, 0, 127, 0.2);
        color: #ff007f;
        border: 1px solid rgba(255, 0, 127, 0.5);
    }

    .badge-amber {
        background: rgba(245, 158, 11, 0.2);
        color: #fbbf24;
        border: 1px solid rgba(245, 158, 11, 0.5);
    }

    /* Streamlit Form Input Styling */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background-color: rgba(10, 4, 22, 0.9) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1px solid rgba(0, 242, 254, 0.3) !important;
        font-weight: 600 !important;
    }

    .stTextInput input:focus, .stNumberInput input:focus, .stSelectbox select:focus {
        border-color: #00f2fe !important;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.6) !important;
    }

    .stButton > button {
        border-radius: 14px !important;
        font-weight: 700 !important;
        padding: 12px 26px !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #00f2fe 0%, #0072ff 100%) !important;
        color: #030712 !important;
        border: none !important;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.5) !important;
    }

    .stButton > button[kind="primary"]:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.8) !important;
    }

    /* Footer styling */
    .footer-container {
        margin-top: 50px;
        padding-top: 25px;
        border-top: 1px solid rgba(0, 242, 254, 0.2);
        text-align: center;
        color: #94a3b8;
        font-size: 0.85rem;
    }
    </style>
    """, unsafe_allow_html=True)

def render_header(title, subtitle, icon="🏎️", tag="CYBERPUNK AI PLATFORM"):
    """Renders a sleek top hero header in Cyberpunk design."""
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, rgba(20, 8, 40, 0.95) 0%, rgba(8, 2, 18, 0.98) 100%);
        border: 1px solid rgba(0, 242, 254, 0.35);
        padding: 32px 38px;
        border-radius: 24px;
        margin-bottom: 25px;
        box-shadow: 0 0 30px rgba(0, 242, 254, 0.25);
        position: relative;
        overflow: hidden;
    ">
        <div style="position: absolute; right: -30px; top: -30px; width: 220px; height: 220px; background: radial-gradient(circle, rgba(0,242,254,0.2) 0%, rgba(0,0,0,0) 70%); border-radius: 50%;"></div>
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
            <div>
                <span class="badge badge-blue">{tag}</span>
                <h1 style="
                    font-family: 'Outfit', sans-serif;
                    font-size: 2.6rem;
                    font-weight: 900;
                    margin: 10px 0 6px 0;
                    color: #ffffff;
                    text-shadow: 0 0 15px rgba(0, 242, 254, 0.5);
                    letter-spacing: -0.5px;
                ">
                    {icon} {title}
                </h1>
                <p style="color: #cbd5e1; font-size: 1.05rem; margin: 0; max-width: 750px;">
                    {subtitle}
                </p>
            </div>
            <div style="text-align: right;">
                <span style="font-size: 0.82rem; color: #00f2fe; font-weight: 700; background: rgba(0,242,254,0.15); padding: 8px 16px; border-radius: 30px; border: 1px solid rgba(0,242,254,0.4); text-shadow: 0 0 8px rgba(0,242,254,0.6);">
                    ⚡ SYSTEM ONLINE
                </span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_footer():
    """Renders professional cyberpunk footer."""
    st.markdown("""
    <div class="footer-container">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; max-width: 1100px; margin: 0 auto;">
            <div>
                <strong style="color: #00f2fe; font-size: 1rem;">AutoDriven Cyberpunk AI Platform</strong><br>
                <span>Automobile Intelligence, Pricing & Segmentation Engine</span>
            </div>
            <div>
                <span>Powered by Streamlit, Scikit-Learn & Plotly</span><br>
                <span>© 2026 Chandrashekar Jadhav. All rights reserved.</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
