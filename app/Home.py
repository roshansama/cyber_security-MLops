import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Adaptive IDS Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================
# LOAD CSS
# =====================================

with open(
    "app/assets/styles.css",
    encoding="utf-8"
) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


# =====================================
# ANIMATED BACKGROUND
# =====================================

background_html = """

<div class="cyber-grid"></div>

<div class="bg-orb orb1"></div>

<div class="bg-orb orb2"></div>

<div class="bg-orb orb3"></div>

"""

st.markdown(
    background_html,
    unsafe_allow_html=True
)


# =====================================
# LOAD DRIFT DATA
# =====================================

drift_df = pd.read_csv(
    r"D:\MLOPS\data\processed\psi_drift_results.csv"
)


# =====================================
# NAVBAR
# =====================================

navbar_html = """

<div class="top-navbar">

<div style="
display:flex;
align-items:center;
gap:14px;
">

<div style="
width:42px;
height:42px;
border-radius:14px;
background:linear-gradient(135deg,#00f0ff,#2563eb);
display:flex;
justify-content:center;
align-items:center;
font-size:20px;
font-weight:800;
box-shadow:0 0 20px rgba(0,240,255,0.3);
">

🛡️

</div>

<div>

<div style="
font-size:18px;
font-weight:800;
color:white;
letter-spacing:1px;
">

ADAPTIVE IDS

</div>

<div style="
font-size:12px;
color:#94a3b8;
">

Enterprise AI Cybersecurity Platform

</div>

</div>

</div>


<div class="nav-links">

<div class="nav-link">Dashboard</div>

<div class="nav-link">Threat Intel</div>

<div class="nav-link">Drift Monitoring</div>

<div class="nav-link">Explainability</div>

<div class="nav-link">Batch Inference</div>

</div>


<div class="system-badge">

<div class="glow-dot"></div>

SYSTEM OPERATIONAL

</div>

</div>

"""

st.markdown(
    navbar_html,
    unsafe_allow_html=True
)


# =====================================
# FLOATING ANALYTICS PANELS
# =====================================

analytics_html = """

<div style="
display:grid;
grid-template-columns:
repeat(auto-fit,minmax(240px,1fr));
gap:20px;
margin-bottom:30px;
">

<div class="floating-panel">

<div class="analytics-label">
Threats Blocked
</div>

<div class="analytics-value">
14,239
</div>

<div class="analytics-trend-up">
↑ 12.4% from previous cycle
</div>

</div>


<div class="floating-panel">

<div class="analytics-label">
Detection Confidence
</div>

<div class="analytics-value">
99.92%
</div>

<div class="analytics-trend-up">
Model stability optimal
</div>

</div>


<div class="floating-panel">

<div class="analytics-label">
Drift Severity
</div>

<div class="analytics-value">
0.59 PSI
</div>

<div class="analytics-trend-down">
Moderate distribution shift
</div>

</div>


<div class="floating-panel">

<div class="analytics-label">
Inference Latency
</div>

<div class="analytics-value">
12ms
</div>

<div class="analytics-trend-up">
FastAPI serving stable
</div>

</div>

</div>

"""

st.markdown(
    analytics_html,
    unsafe_allow_html=True
)


# =====================================
# HERO SECTION
# =====================================

hero_html = """

<div class="glass-card">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
gap:50px;
flex-wrap:wrap;
">

<div style="
flex:1;
min-width:320px;
">

<div style="
display:inline-block;
padding:8px 16px;
border-radius:30px;
border:1px solid rgba(0,240,255,0.3);
background:rgba(0,240,255,0.08);
color:#00f0ff;
font-size:12px;
font-weight:700;
letter-spacing:1px;
margin-bottom:20px;
">

ENTERPRISE AI SECURITY PLATFORM

</div>

<h1>

Adaptive AI for <br>

<span class="gradient-text">

Real-Time Cyber Threat Detection

</span>

</h1>

<p style="
font-size:20px;
line-height:1.8;
color:#94a3b8;
max-width:700px;
margin-top:20px;
">

Drift-aware intrusion detection platform combining explainable AI, adaptive retraining, real-time inference, and enterprise-grade MLOps infrastructure.

</p>

</div>


<div style="
flex:1;
min-width:300px;
display:flex;
justify-content:center;
align-items:center;
position:relative;
height:450px;
">

<div style="
width:340px;
height:340px;
border-radius:50%;
border:1px solid rgba(0,240,255,0.2);
position:absolute;
box-shadow:0 0 50px rgba(0,240,255,0.15);
">

</div>

<div style="
width:250px;
height:250px;
border-radius:50%;
border:1px dashed rgba(181,53,246,0.4);
position:absolute;
animation:spin 18s linear infinite;
">

</div>

<div style="
width:170px;
height:170px;
border-radius:50%;
background:rgba(0,240,255,0.08);
border:1px solid rgba(0,240,255,0.3);
backdrop-filter:blur(12px);
display:flex;
justify-content:center;
align-items:center;
font-size:70px;
box-shadow:0 0 40px rgba(0,240,255,0.2);
">

🛡️

</div>

</div>

</div>

</div>

<style>

@keyframes spin {

from {

transform:rotate(0deg);

}

to {

transform:rotate(360deg);

}

}

</style>

"""

st.markdown(
    hero_html,
    unsafe_allow_html=True
)


# =====================================
# THREAT INTELLIGENCE
# =====================================

st.markdown(
    '<div class="section-spacing"></div>',
    unsafe_allow_html=True
)

st.markdown("""

<div class="glass-card">

<h2>
📈 Threat Intelligence Snapshot
</h2>

</div>

""", unsafe_allow_html=True)


labels = [
    "Benign",
    "DDoS",
    "Port Scan",
    "Botnet",
    "Brute Force"
]

values = [
    72,
    11,
    7,
    6,
    4
]


fig = go.Figure(
    data=[
        go.Pie(
            labels=labels,
            values=values,
            hole=0.65
        )
    ]
)

fig.update_layout(
    paper_bgcolor="#050b14",
    plot_bgcolor="#050b14",
    font_color="white",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# =====================================
# PIPELINE ARCHITECTURE
# =====================================

st.markdown(
    '<div class="section-spacing"></div>',
    unsafe_allow_html=True
)

pipeline_html = """

<div class="glass-card">

<h2>
⚙️ Adaptive AI Pipeline
</h2>

<br>

<div style="
display:flex;
justify-content:space-between;
align-items:center;
gap:18px;
flex-wrap:wrap;
">

<div class="pipeline-node">
📡<br><br>
Traffic Data
</div>

<div style="font-size:28px;color:#00f0ff;">→</div>

<div class="pipeline-node">
🧠<br><br>
Feature Engineering
</div>

<div style="font-size:28px;color:#00f0ff;">→</div>

<div class="pipeline-node">
🤖<br><br>
XGBoost Detection
</div>

<div style="font-size:28px;color:#00f0ff;">→</div>

<div class="pipeline-node">
🔬<br><br>
SHAP Explainability
</div>

<div style="font-size:28px;color:#00f0ff;">→</div>

<div class="pipeline-node">
📈<br><br>
Drift Monitoring
</div>

<div style="font-size:28px;color:#00f0ff;">→</div>

<div class="pipeline-node">
♻️<br><br>
Adaptive Retraining
</div>

</div>

</div>

"""

st.markdown(
    pipeline_html,
    unsafe_allow_html=True
)


# =====================================
# SHAP EXPLAINABILITY
# =====================================

st.markdown(
    '<div class="section-spacing"></div>',
    unsafe_allow_html=True
)

left, right = st.columns(2)


with left:

    st.markdown("""

<div class="glass-card">

<h2>
🔬 Explainable AI
</h2>

<br>

Payload Length
<div class="shap-bar" style="width:90%;"></div>

<br>

Packet Variance
<div class="shap-bar" style="width:72%;"></div>

<br>

Destination Port
<div class="shap-bar" style="width:58%;"></div>

<br>

Flow Duration
<div class="shap-bar" style="width:44%;"></div>

</div>

""", unsafe_allow_html=True)


with right:

    st.markdown("""

<div class="glass-card">

<h2>
🧠 Analyst Transparency
</h2>

<p style="
color:#cbd5e1;
line-height:1.9;
font-size:16px;
">

Adaptive IDS provides transparent AI-driven threat explanations using SHAP feature attribution.

Security analysts can understand:
• Why a payload was classified as malicious
• Which traffic behaviors triggered alerts
• Which features contributed most strongly

</p>

</div>

""", unsafe_allow_html=True)


# =====================================
# LIVE SOC OPERATIONS
# =====================================

st.markdown(
    '<div class="section-spacing"></div>',
    unsafe_allow_html=True
)

left_feed, right_feed = st.columns([1.2, 1])


with left_feed:

    st.markdown("""

<div class="glass-card">

<h2>
🚨 Threat Activity Feed
</h2>

<div class="feed-item">
<div class="threat-critical">
CRITICAL — DDoS Attack Pattern
</div>

<div style="color:#94a3b8;font-size:13px;margin-top:6px;">
Detected anomalous packet burst behavior targeting Port 443.
</div>
</div>


<div class="feed-item">
<div class="threat-medium">
MEDIUM — Port Scanning Activity
</div>

<div style="color:#94a3b8;font-size:13px;margin-top:6px;">
Sequential destination port probing detected across subnet.
</div>
</div>


<div class="feed-item">
<div class="threat-low">
LOW — Drift Threshold Monitoring
</div>

<div style="color:#94a3b8;font-size:13px;margin-top:6px;">
Population Stability Index approaching adaptive threshold.
</div>
</div>

</div>

""", unsafe_allow_html=True)


with right_feed:

    st.markdown("""

<div class="glass-card">

<h2>
⚡ Infrastructure Health
</h2>

<br>

<div style="display:flex;justify-content:space-between;">
<div>API Gateway</div>
<div style="color:#00ff66;font-weight:700;">ONLINE</div>
</div>

<br>

<div style="display:flex;justify-content:space-between;">
<div>Inference Engine</div>
<div style="color:#00ff66;font-weight:700;">ACTIVE</div>
</div>

<br>

<div style="display:flex;justify-content:space-between;">
<div>Drift Monitoring</div>
<div style="color:#facc15;font-weight:700;">MODERATE</div>
</div>

<br>

<div style="display:flex;justify-content:space-between;">
<div>Adaptive Retraining</div>
<div style="color:#00f0ff;font-weight:700;">READY</div>
</div>

</div>

""", unsafe_allow_html=True)


# =====================================
# DRIFT INTELLIGENCE
# =====================================

st.markdown(
    '<div class="section-spacing"></div>',
    unsafe_allow_html=True
)

top_drift = drift_df.sort_values(
    by="PSI Score",
    ascending=False
).head(10)


drift_fig = go.Figure()

drift_fig.add_trace(
    go.Bar(
        x=top_drift["PSI Score"],
        y=top_drift["Feature"],
        orientation="h",
        marker=dict(
            color=top_drift["PSI Score"],
            colorscale="Turbo"
        )
    )
)

drift_fig.update_layout(
    paper_bgcolor="#050b14",
    plot_bgcolor="#050b14",
    font_color="white",
    height=600,
    yaxis=dict(autorange="reversed")
)

st.plotly_chart(
    drift_fig,
    use_container_width=True
)
# =====================================
# MODEL PERFORMANCE INTELLIGENCE
# =====================================

st.markdown(
    '<div class="section-spacing"></div>',
    unsafe_allow_html=True
)


st.markdown("""

<div class="glass-card">

<h2>

🧠 AI Model Intelligence

</h2>

<p style="
color:#94a3b8;
font-size:16px;
">

Enterprise observability metrics for adaptive intrusion detection performance.

</p>

</div>

""", unsafe_allow_html=True)


categories = [

    "Accuracy",

    "Precision",

    "Recall",

    "F1 Score",

    "ROC-AUC",

    "Latency"
]


values = [

    99.92,

    99.68,

    99.83,

    99.76,

    99.99,

    88
]


radar_fig = go.Figure()


radar_fig.add_trace(

    go.Scatterpolar(

        r=values,

        theta=categories,

        fill='toself',

        line=dict(
            color="#00f0ff",
            width=3
        ),

        fillcolor="rgba(0,240,255,0.2)"
    )
)


radar_fig.update_layout(

    polar=dict(

        bgcolor="#050b14",

        radialaxis=dict(

            visible=True,

            range=[0, 100],

            gridcolor="rgba(255,255,255,0.08)",

            linecolor="rgba(255,255,255,0.08)"
        )
    ),

    paper_bgcolor="#050b14",

    font_color="white",

    height=600
)


st.plotly_chart(
    radar_fig,
    use_container_width=True
)

# =====================================
# GLOBAL THREAT MAP
# =====================================

st.markdown(
    '<div class="section-spacing"></div>',
    unsafe_allow_html=True
)

np.random.seed(42)

latitudes = np.random.uniform(-60, 75, 120)
longitudes = np.random.uniform(-180, 180, 120)
intensity = np.random.uniform(10, 100, 120)


geo_fig = go.Figure(

    data=go.Scattergeo(

        lon=longitudes,
        lat=latitudes,

        mode='markers',

        marker=dict(
            size=intensity / 6,
            color=intensity,
            colorscale='Turbo',
            opacity=0.75
        )
    )
)

geo_fig.update_layout(
    paper_bgcolor="#050b14",
    plot_bgcolor="#050b14",
    font_color="white",
    height=700,

    geo=dict(
        bgcolor="#050b14",
        showland=True,
        landcolor="#0f172a",
        showocean=True,
        oceancolor="#020617",
        showcountries=True,
        projection_type="natural earth"
    )
)

st.plotly_chart(
    geo_fig,
    use_container_width=True
)


# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "Adaptive IDS Platform | Explainable AI + Drift Intelligence + Enterprise MLOps"
)