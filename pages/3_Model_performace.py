import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Model Performance",
    page_icon="📈",
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
BASE_DIR = Path(__file__).parent.parent

st.title("📈 Machine Learning Model Performance")

st.markdown("""
<div style='background: linear-gradient(90deg,#0f172a,#2563eb);
padding:25px;
border-radius:15px;'>

<h2 style='color:white;text-align:center;'>
Model Comparison Dashboard
</h2>

<p style='color:white;text-align:center;'>
Performance Comparison of Regression Models
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Linear Regression", "0.6201")

with col2:
    st.metric("Random Forest", "0.9729")

with col3:
    st.metric("Gradient Boosting", "0.9583")

st.success("🏆 Best Performing Model: Gradient Boosting")

st.markdown("---")

st.subheader("📊 Model Comparison")

img = BASE_DIR / "model_comparison.png"

if img.exists():
    st.image(str(img), use_container_width=True)

st.markdown("---")

st.subheader("🎯 Actual vs Predicted")

img = BASE_DIR / "actual_vs_predicted.png"

if img.exists():
    st.image(str(img), use_container_width=True)

st.markdown("---")

st.subheader("⭐ Feature Importance")

img = BASE_DIR / "feature_importance.png"

if img.exists():
    st.image(str(img), use_container_width=True)

st.markdown("---")

st.markdown("""
### Conclusion

✅ Gradient Boosting achieved the best balance of accuracy and generalization.

✅ Random Forest also performed very well.

✅ Linear Regression serves as a baseline model.

✅ Final model selected for deployment: Gradient Boosting Regressor.
""")

st.markdown("---")

st.markdown("""
<center>
<h3>🚘 AutoIntel</h3>
<p>Model Performance Analysis Module</p>
</center>
""", unsafe_allow_html=True)