import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Market Segmentation",
    page_icon="📊",
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

st.title("📊 Automobile Market Segmentation")

st.markdown("""
<div style='background: linear-gradient(90deg,#0f172a,#2563eb);
padding:25px;
border-radius:15px;'>

<h2 style='color:white;text-align:center;'>
Customer Market Segmentation Analysis
</h2>

<p style='color:white;text-align:center;'>
K-Means Clustering Based Customer Segmentation
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Cars", "11,914")

with col2:
    st.metric("Clusters", "3")

with col3:
    st.metric("Algorithm", "K-Means")

st.markdown("---")

st.subheader("📈 Cluster Visualization")

image_path = BASE_DIR / "cluster_visualization.png"

if image_path.exists():
    st.image(str(image_path), use_container_width=True)

st.markdown("---")

st.subheader("🚗 Customer Segments")

c1, c2, c3 = st.columns(3)

with c1:
    st.info("""
### Economy Commuters

💰 Avg Price: $23,565

⚙️ Avg HP: 170

⛽ Highway MPG: 33
""")

with c2:
    st.success("""
### Mid-Range Family

💰 Avg Price: $39,171

⚙️ Avg HP: 290

⛽ Highway MPG: 23
""")

with c3:
    st.warning("""
### Luxury Sports

💰 Avg Price: $219,890

⚙️ Avg HP: 545

⛽ Highway MPG: 19
""")

st.markdown("---")

st.markdown("""
<center>
<h3>🚘 AutoIntel</h3>
<p>Market Segmentation Module</p>
</center>
""", unsafe_allow_html=True)