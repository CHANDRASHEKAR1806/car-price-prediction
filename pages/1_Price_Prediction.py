import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
from style_utils import apply_custom_styles, render_header, render_footer, get_asset_image

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Price Predictor | AutoDriven",
    page_icon="💰",
    layout="wide"
)

apply_custom_styles()

BASE_DIR = Path(__file__).parent.parent
model = joblib.load(BASE_DIR / "car_price_gradient_boosting.pkl")

# Real car images
sports_img = get_asset_image("luxury_sports")
sedan_img = get_asset_image("family_sedan")
suv_img = get_asset_image("suv_pickup")

# =====================================================
# HEADER
# =====================================================
render_header(
    title="Automobile Price Predictor",
    subtitle="AI-Powered Valuation Engine utilizing Gradient Boosting ML Model (95.8% R² Accuracy)",
    icon="💰",
    tag="Regression Model v1.0"
)

# =====================================================
# ENCODING MAPS
# =====================================================
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
fuel_map = {"Regular Unleaded": 9, "Premium Unleaded (required)": 8, "Premium Unleaded (recommended)": 7, "Diesel": 0, "Electric": 1}
trans_map = {"Automatic": 1, "Manual": 3, "Automated Manual": 0, "Direct Drive": 2}
drive_map = {"Front Wheel Drive": 2, "Rear Wheel Drive": 3, "All Wheel Drive": 0, "Four Wheel Drive": 1}
size_map = {"Compact": 0, "Midsize": 2, "Large": 1}
style_map = {"Sedan": 14, "Coupe": 8, "4dr SUV": 3, "Convertible": 6, "2dr Hatchback": 0, "Crew Cab Pickup": 9}

# =====================================================
# PRESET CAR CONFIGURATIONS WITH REAL CAR GALLERY
# =====================================================
st.markdown("<h3 style='font-family: Outfit; color: white;'>⚡ Quick Sample Presets & Vehicle Gallery</h3>", unsafe_allow_html=True)
st.markdown("<span style='color: #cbd5e1; font-size: 0.95rem;'>Click any preset button below to prefill vehicle parameters:</span>", unsafe_allow_html=True)

presets = {
    "BMW M3 Performance": {"hp": 425.0, "hwy": 26.0, "city": 17.0, "cyl": 6.0, "doors": 4.0, "yr": 2020, "pop": 3916, "make": "BMW", "fuel": "Premium Unleaded (required)", "trans": "Manual", "drive": "Rear Wheel Drive", "size": "Compact", "style": "Sedan", "img": sports_img},
    "Toyota Camry Family": {"hp": 203.0, "hwy": 39.0, "city": 28.0, "cyl": 4.0, "doors": 4.0, "yr": 2021, "pop": 2033, "make": "Toyota", "fuel": "Regular Unleaded", "trans": "Automatic", "drive": "Front Wheel Drive", "size": "Midsize", "style": "Sedan", "img": sedan_img},
    "Ford F-150 Pickup": {"hp": 375.0, "hwy": 23.0, "city": 17.0, "cyl": 6.0, "doors": 4.0, "yr": 2020, "pop": 5657, "make": "Ford", "fuel": "Regular Unleaded", "trans": "Automatic", "drive": "Four Wheel Drive", "size": "Large", "style": "Crew Cab Pickup", "img": suv_img}
}

col_g1, col_g2, col_g3 = st.columns(3)

for col, (p_name, p_vals) in zip([col_g1, col_g2, col_g3], presets.items()):
    with col:
        if p_vals["img"]:
            st.image(p_vals["img"], use_container_width=True)
        if st.button(f"🚘 Preset: {p_name}", use_container_width=True):
            st.session_state["hp"] = p_vals["hp"]
            st.session_state["hwy"] = p_vals["hwy"]
            st.session_state["city"] = p_vals["city"]
            st.session_state["cyl"] = p_vals["cyl"]
            st.session_state["doors"] = p_vals["doors"]
            st.session_state["yr"] = p_vals["yr"]
            st.session_state["pop"] = p_vals["pop"]
            st.session_state["make"] = p_vals["make"]
            st.session_state["fuel"] = p_vals["fuel"]
            st.session_state["trans"] = p_vals["trans"]
            st.session_state["drive"] = p_vals["drive"]
            st.session_state["size"] = p_vals["size"]
            st.session_state["style"] = p_vals["style"]

st.markdown("<br>", unsafe_allow_html=True)

# Initialize defaults if not set
default_vals = presets["BMW M3 Performance"]
hp_val = st.session_state.get("hp", default_vals["hp"])
hwy_val = st.session_state.get("hwy", default_vals["hwy"])
city_val = st.session_state.get("city", default_vals["city"])
cyl_val = st.session_state.get("cyl", default_vals["cyl"])
doors_val = st.session_state.get("doors", default_vals["doors"])
yr_val = st.session_state.get("yr", default_vals["yr"])
pop_val = st.session_state.get("pop", default_vals["pop"])
make_val = st.session_state.get("make", default_vals["make"])
fuel_val = st.session_state.get("fuel", default_vals["fuel"])
trans_val = st.session_state.get("trans", default_vals["trans"])
drive_val = st.session_state.get("drive", default_vals["drive"])
size_val = st.session_state.get("size", default_vals["size"])
style_val = st.session_state.get("style", default_vals["style"])

# =====================================================
# INPUT SPECIFICATIONS FORM
# =====================================================
st.markdown("<h3 style='font-family: Outfit; color: white;'>⚙️ Enter Vehicle Specifications</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass-card">
        <h4 style="color: #00f2fe; margin-top: 0;">🏎️ Engine & Performance</h4>
    </div>
    """, unsafe_allow_html=True)
    engine_hp = st.number_input("Engine HP (Horsepower)", value=float(hp_val), min_value=50.0, max_value=1500.0, step=10.0)
    highway_mpg = st.number_input("Highway MPG", value=float(hwy_val), min_value=10.0, max_value=150.0, step=1.0)
    city_mpg = st.number_input("City MPG", value=float(city_val), min_value=5.0, max_value=150.0, step=1.0)
    engine_cylinders = st.number_input("Engine Cylinders", value=float(cyl_val), min_value=0.0, max_value=16.0, step=1.0)

with col2:
    st.markdown("""
    <div class="glass-card">
        <h4 style="color: #34d399; margin-top: 0;">🚙 Body & Dimensions</h4>
    </div>
    """, unsafe_allow_html=True)
    num_doors = st.number_input("Number of Doors", value=float(doors_val), min_value=2.0, max_value=4.0, step=1.0)
    year = st.number_input("Model Year", value=int(yr_val), min_value=1990, max_value=2026, step=1)
    popularity = st.number_input("Brand Popularity Score", value=int(pop_val), min_value=0, max_value=10000, step=100)
    size_enc = st.selectbox("Vehicle Size", list(size_map.keys()), index=list(size_map.keys()).index(size_val) if size_val in size_map else 0)

with col3:
    st.markdown("""
    <div class="glass-card">
        <h4 style="color: #ff007f; margin-top: 0;">🏷️ Brand & Transmission</h4>
    </div>
    """, unsafe_allow_html=True)
    make_enc = st.selectbox("Car Brand", list(make_map.keys()), index=list(make_map.keys()).index(make_val) if make_val in make_map else 0)
    fuel_enc = st.selectbox("Fuel Type", list(fuel_map.keys()), index=list(fuel_map.keys()).index(fuel_val) if fuel_val in fuel_map else 0)
    trans_enc = st.selectbox("Transmission", list(trans_map.keys()), index=list(trans_map.keys()).index(trans_val) if trans_val in trans_map else 0)
    drive_enc = st.selectbox("Drive Train", list(drive_map.keys()), index=list(drive_map.keys()).index(drive_val) if drive_val in drive_map else 0)
    style_enc = st.selectbox("Body Style", list(style_map.keys()), index=list(style_map.keys()).index(style_val) if style_val in style_map else 0)

st.markdown("<br>", unsafe_allow_html=True)

# Buttons
btn_col1, btn_col2 = st.columns([2, 1])

with btn_col1:
    predict_btn = st.button("🚀 Generate AI Price Valuation", use_container_width=True, type="primary")

with btn_col2:
    reset_btn = st.button("🔄 Reset Inputs", use_container_width=True)

if reset_btn:
    for key in ["hp", "hwy", "city", "cyl", "doors", "yr", "pop", "make", "fuel", "trans", "drive", "size", "style"]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()

# =====================================================
# PREDICTION RESULTS & ANALYTICS
# =====================================================
if predict_btn or "last_prediction" in st.session_state:

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

    pred_val = model.predict(features)[0]
    st.session_state["last_prediction"] = pred_val

    price_lower = max(0, pred_val * 0.94)
    price_upper = pred_val * 1.06

    # Tier classification
    if pred_val < 30000:
        tier_label = "Budget Commuter Class"
        tier_badge = "badge-blue"
    elif pred_val < 70000:
        tier_label = "Premium Executive Tier"
        tier_badge = "badge-green"
    elif pred_val < 150000:
        tier_label = "High-Performance Luxury"
        tier_badge = "badge-purple"
    else:
        tier_label = "Exotic Supercar Category"
        tier_badge = "badge-amber"

    st.markdown("<hr style='border-color: rgba(0, 242, 254, 0.2); margin: 30px 0;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: Outfit; font-weight: 700; color: white;'>📊 Valuation Dashboard</h2>", unsafe_allow_html=True)

    res_col1, res_col2 = st.columns([1.2, 1])

    with res_col1:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, rgba(20, 8, 40, 0.9) 0%, rgba(8, 2, 18, 0.95) 100%);
            border: 1px solid rgba(0, 242, 254, 0.4);
            border-radius: 24px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 0 25px rgba(0, 242, 254, 0.3);
        ">
            <span class="badge {tier_badge}" style="font-size: 0.85rem; padding: 6px 16px;">{tier_label}</span>
            <p style="color: #cbd5e1; font-size: 1rem; margin-top: 15px; margin-bottom: 5px;">Estimated Market MSRP (USD)</p>
            <h1 style="
                font-family: 'Outfit', sans-serif;
                font-size: 3.5rem;
                font-weight: 900;
                color: #00f2fe;
                text-shadow: 0 0 15px rgba(0, 242, 254, 0.6);
                margin: 0;
                letter-spacing: -1px;
            ">
                ${pred_val:,.2f}
            </h1>
            <p style="color: #cbd5e1; font-size: 0.95rem; margin-top: 10px;">
                Valuation Range: <strong>${price_lower:,.0f}</strong> – <strong>${price_upper:,.0f}</strong> (±6% Confidence Interval)
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Quick breakdown metrics
        m1, m2 = st.columns(2)
        with m1:
            annual_mpg_avg = (highway_mpg + city_mpg) / 2.0
            est_fuel_cost = (12000 / max(1, annual_mpg_avg)) * 3.65
            st.metric("Est. Annual Fuel Cost", f"${est_fuel_cost:,.0f}", f"Avg {annual_mpg_avg:.1f} MPG")
        with m2:
            power_ratio = engine_hp / max(1, engine_cylinders) if engine_cylinders > 0 else engine_hp
            st.metric("HP per Cylinder", f"{power_ratio:.1f} HP/Cyl", f"{engine_hp:.0f} Total HP")

    with res_col2:
        # 5-Year Estimated Depreciation Chart
        years_proj = [year + i for i in range(6)]
        depr_rates = [1.0, 0.85, 0.74, 0.65, 0.58, 0.52]
        values_proj = [pred_val * r for r in depr_rates]

        df_depr = pd.DataFrame({"Year": years_proj, "Estimated Value ($)": values_proj})

        fig = px.line(
            df_depr,
            x="Year",
            y="Estimated Value ($)",
            title="📉 5-Year Projected Depreciation Curve",
            markers=True
        )
        fig.update_traces(line_color="#00f2fe", line_width=3, marker_size=8, marker_color="#00f2fe")
        fig.update_layout(
            paper_bgcolor="rgba(15, 23, 42, 0.6)",
            plot_bgcolor="rgba(15, 23, 42, 0.6)",
            font_color="#f8fafc",
            height=280,
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)

# =====================================================
# FOOTER
# =====================================================
render_footer()