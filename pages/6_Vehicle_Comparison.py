import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
from pathlib import Path
from style_utils import apply_custom_styles, render_header, render_footer, get_asset_image

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Vehicle Comparison | AutoDriven",
    page_icon="⚖️",
    layout="wide"
)

apply_custom_styles()

BASE_DIR = Path(__file__).parent.parent

# Fail-Safe Model Loader with Automatic On-The-Fly Fallback
@st.cache_resource
def load_or_train_gbm():
    model_path = BASE_DIR / "car_price_gradient_boosting.pkl"
    try:
        return joblib.load(model_path)
    except Exception:
        data_path = BASE_DIR / "data.csv"
        if not data_path.exists():
            return None
        df = pd.read_csv(data_path)
        feature_cols = [
            'Engine HP', 'highway MPG', 'city mpg', 'Engine Cylinders', 
            'Number of Doors', 'Year', 'Popularity', 'Make', 
            'Engine Fuel Type', 'Transmission Type', 'Driven_Wheels', 
            'Vehicle Size', 'Vehicle Style'
        ]
        for col in ['Engine HP', 'Engine Cylinders', 'Number of Doors', 'highway MPG', 'city mpg', 'Popularity', 'Year', 'MSRP']:
            if col in df.columns:
                df[col] = df[col].fillna(df[col].median())
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        for c in ['Make', 'Engine Fuel Type', 'Transmission Type', 'Driven_Wheels', 'Vehicle Size', 'Vehicle Style']:
            if c in df.columns:
                df[c] = le.fit_transform(df[c].astype(str))
        X = df[feature_cols].values
        y = df['MSRP'].values
        from sklearn.ensemble import GradientBoostingRegressor
        gbm = GradientBoostingRegressor(n_estimators=80, random_state=42)
        gbm.fit(X, y)
        return gbm

model = load_or_train_gbm()

# Real car images
sports_img = get_asset_image("luxury_sports")
sedan_img = get_asset_image("family_sedan")
suv_img = get_asset_image("suv_pickup")

# Encoding maps
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
style_map = {"Sedan": 14, "Coupe": 8, "4dr SUV": 3, "Convertible": 6, "2dr Hatchback": 0}

# =====================================================
# HEADER
# =====================================================
render_header(
    title="Side-by-Side Vehicle Comparison Matrix",
    subtitle="Configure two custom vehicle specifications to compare AI predicted prices, fuel costs, and performance side-by-side",
    icon="⚖️",
    tag="Multi-Vehicle Evaluation"
)

# =====================================================
# INPUT COLUMNS WITH REAL CAR IMAGES
# =====================================================
col_a, col_b = st.columns(2)

with col_a:
    if sedan_img:
        st.image(sedan_img, caption="🚘 Configuration A Vehicle", use_container_width=True)
    st.markdown("""
    <div class="glass-card" style="border-color: rgba(0, 242, 254, 0.4);">
        <h3 style="color: #00f2fe; margin-top: 0; font-family: Outfit;">🚘 Vehicle Configuration A</h3>
    </div>
    """, unsafe_allow_html=True)
    make_a = st.selectbox("Brand A", list(make_map.keys()), index=4, key="make_a")
    hp_a = st.number_input("Horsepower (HP)", value=300.0, step=10.0, key="hp_a")
    hwy_a = st.number_input("Highway MPG", value=28.0, step=1.0, key="hwy_a")
    city_a = st.number_input("City MPG", value=20.0, step=1.0, key="city_a")
    cyl_a = st.number_input("Cylinders", value=6.0, step=1.0, key="cyl_a")
    yr_a = st.number_input("Year", value=2021, step=1, key="yr_a")
    style_a = st.selectbox("Body Style A", list(style_map.keys()), index=0, key="style_a")

with col_b:
    if sports_img:
        st.image(sports_img, caption="🏎️ Configuration B Vehicle", use_container_width=True)
    st.markdown("""
    <div class="glass-card" style="border-color: rgba(255, 0, 127, 0.4);">
        <h3 style="color: #ff007f; margin-top: 0; font-family: Outfit;">🏎️ Vehicle Configuration B</h3>
    </div>
    """, unsafe_allow_html=True)
    make_b = st.selectbox("Brand B", list(make_map.keys()), index=37, key="make_b")
    hp_b = st.number_input("Horsepower (HP)", value=440.0, step=10.0, key="hp_b")
    hwy_b = st.number_input("Highway MPG", value=24.0, step=1.0, key="hwy_b")
    city_b = st.number_input("City MPG", value=17.0, step=1.0, key="city_b")
    cyl_b = st.number_input("Cylinders", value=6.0, step=1.0, key="cyl_b")
    yr_b = st.number_input("Year", value=2022, step=1, key="yr_b")
    style_b = st.selectbox("Body Style B", list(style_map.keys()), index=1, key="style_b")

# =====================================================
# PREDICTION & COMPARISON
# =====================================================
st.markdown("<br>", unsafe_allow_html=True)

if model is not None:
    feat_a = np.array([[hp_a, hwy_a, city_a, cyl_a, 4.0, yr_a, 2000, make_map[make_a], 8, 1, 3, 2, style_map[style_a]]])
    feat_b = np.array([[hp_b, hwy_b, city_b, cyl_b, 2.0, yr_b, 2000, make_map[make_b], 8, 1, 3, 0, style_map[style_b]]])

    pred_a = float(model.predict(feat_a)[0])
    pred_b = float(model.predict(feat_b)[0])

    price_diff = pred_b - pred_a
    pct_diff = (price_diff / max(1, pred_a)) * 100

    st.markdown("<h2 style='font-family: Outfit; font-weight: 700; color: white;'>📊 Comparison Summary</h2>", unsafe_allow_html=True)

    res1, res2, res3 = st.columns(3)

    with res1:
        st.markdown(f"""
        <div class="metric-card-pro" style="border-color: rgba(0, 242, 254, 0.4);">
            <div class="metric-label">{make_a} Valuation</div>
            <div class="metric-val" style="color: #00f2fe;">${pred_a:,.2f}</div>
            <div class="metric-sub">{hp_a:.0f} HP • {hwy_a:.0f} MPG</div>
        </div>
        """, unsafe_allow_html=True)

    with res2:
        st.markdown(f"""
        <div class="metric-card-pro" style="border-color: rgba(255, 0, 127, 0.4);">
            <div class="metric-label">{make_b} Valuation</div>
            <div class="metric-val" style="color: #ff007f;">${pred_b:,.2f}</div>
            <div class="metric-sub">{hp_b:.0f} HP • {hwy_b:.0f} MPG</div>
        </div>
        """, unsafe_allow_html=True)

    with res3:
        diff_color = "#ff007f" if price_diff > 0 else "#00f2fe"
        st.markdown(f"""
        <div class="metric-card-pro">
            <div class="metric-label">Valuation Delta</div>
            <div class="metric-val" style="color: {diff_color};">${abs(price_diff):,.2f}</div>
            <div class="metric-sub">{make_b} is {abs(pct_diff):.1f}% {"higher" if price_diff > 0 else "lower"}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Comparison Bar Chart
    fig_comp = go.Figure(data=[
        go.Bar(name=f"{make_a} ({style_a})", x=["Price ($)", "Horsepower (HP)", "Highway MPG"], y=[pred_a, hp_a, hwy_a], marker_color="#00f2fe"),
        go.Bar(name=f"{make_b} ({style_b})", x=["Price ($)", "Horsepower (HP)", "Highway MPG"], y=[pred_b, hp_b, hwy_b], marker_color="#ff007f")
    ])

    fig_comp.update_layout(
        barmode="group",
        title="Side-by-Side Parameter Comparison",
        paper_bgcolor="rgba(15, 23, 42, 0.6)",
        plot_bgcolor="rgba(15, 23, 42, 0.6)",
        font_color="#f8fafc",
        height=400
    )

    st.plotly_chart(fig_comp, use_container_width=True)

# =====================================================
# FOOTER
# =====================================================
render_footer()
