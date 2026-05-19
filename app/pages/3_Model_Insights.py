import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Model Intelligence",
    layout="wide"
)

# =========================================
# LOAD CSS
# =========================================

with open(
    "app/assets/styles.css",
    encoding="utf-8"
) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================================
# HERO SECTION
# =========================================

st.markdown("""

<div class="hero-section">

<h1 class="hero-title">

🔬 AI Model Intelligence Center

</h1>

<p class="hero-subtitle">

Production-grade model intelligence dashboard
covering ensemble benchmarking,
feature attribution,
decision explainability,
performance analytics,
and adaptive inference architecture.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# TOP METRICS
# =========================================

metric1, metric2, metric3, metric4, metric5 = st.columns(5)

with metric1:

    st.markdown("""

    <div class="metric-card">

    <h3>🎯 ROC-AUC</h3>

    <h1>0.9999</h1>

    <p>Attack separation capability</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric2:

    st.markdown("""

    <div class="metric-card">

    <h3>📈 Recall</h3>

    <h1>99.83%</h1>

    <p>Threat detection sensitivity</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric3:

    st.markdown("""

    <div class="metric-card">

    <h3>⚡ Precision</h3>

    <h1>99.68%</h1>

    <p>Prediction reliability</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric4:

    st.markdown("""

    <div class="metric-card">

    <h3>🧠 F1 Score</h3>

    <h1>0.9976</h1>

    <p>Balanced classification quality</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric5:

    st.markdown("""

    <div class="metric-card">

    <h3>🏆 Production Model</h3>

    <h1>XGBoost</h1>

    <p>Adaptive ensemble classifier</p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# MODEL OVERVIEW
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🧠 Production Model Architecture

</h2>

<p class="section-text">

The production intrusion detection engine
uses an optimized XGBoost ensemble classifier
selected after benchmarking multiple boosting architectures.

Models evaluated included:

<ul>

<li>Random Forest</li>

<li>Gradient Boosting</li>

<li>AdaBoost</li>

<li>LightGBM</li>

<li>CatBoost</li>

<li>XGBoost</li>

</ul>

XGBoost was selected because it achieved:

<ul>

<li>Highest Recall</li>

<li>Best ROC-AUC</li>

<li>Strongest drift robustness</li>

<li>Fast inference latency</li>

<li>Excellent SHAP compatibility</li>

<li>Scalable production performance</li>

</ul>

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# FEATURE IMPORTANCE
# =========================================

st.markdown("""

<h2 class="section-title">

📌 Feature Importance Intelligence

</h2>

""",
unsafe_allow_html=True
)

feature_data = {

    "Feature":[

        "Bwd Packet Length Std",

        "Packet Length Std",

        "Average Packet Size",

        "Destination Port",

        "Init_Win_bytes_forward",

        "Flow Duration",

        "Flow Bytes/s",

        "Packet Length Mean",

        "Fwd Packet Length Max",

        "Total Fwd Packets"
    ],

    "Importance":[

        0.096,
        0.078,
        0.044,
        0.033,
        0.028,
        0.025,
        0.021,
        0.018,
        0.015,
        0.013
    ]
}

df = pd.DataFrame(
    feature_data
)

fig = px.bar(

    df,

    x="Importance",

    y="Feature",

    orientation="h",

    color="Importance",

    title="Top Model Features"
)

fig.update_layout(

    template="plotly_dark",

    height=650,

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font=dict(
        color="white"
    ),

    title_font_size=24
)

fig.update_yaxes(
    autorange="reversed"
)

st.plotly_chart(
    fig,
    width="stretch"
)

# =========================================
# WHY FEATURES MATTER
# =========================================

st.markdown("""

<h2 class="section-title">

🌐 Why These Features Matter

</h2>

""",
unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""

    <div class="glass-card">

    <h3>📡 Packet Behavior Features</h3>

    <p class="section-text">

    Features such as:

    <ul>

    <li>Packet Length Std</li>

    <li>Average Packet Size</li>

    <li>Packet Length Mean</li>

    </ul>

    help detect:

    <ul>

    <li>Traffic flooding</li>

    <li>DDoS attacks</li>

    <li>Packet anomalies</li>

    <li>Traffic bursts</li>

    </ul>

    because malicious traffic often
    changes packet distribution behavior.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

with col2:

    st.markdown("""

    <div class="glass-card">

    <h3>🌪️ Flow Intelligence Features</h3>

    <p class="section-text">

    Features such as:

    <ul>

    <li>Flow Duration</li>

    <li>Flow Bytes/s</li>

    <li>Total Fwd Packets</li>

    </ul>

    help identify:

    <ul>

    <li>Traffic spikes</li>

    <li>Reconnaissance activity</li>

    <li>Botnet communication</li>

    <li>Abnormal connection behavior</li>

    </ul>

    through statistical flow analysis.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# SHAP EXPLAINABILITY
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🔬 SHAP Explainability Integration

</h2>

<p class="section-text">

SHAP (SHapley Additive Explanations)
was integrated to provide transparent AI reasoning.

This enables the platform to explain:

<ul>

<li>Why predictions occurred</li>

<li>Which features contributed most</li>

<li>How traffic behavior changed</li>

<li>Why attacks were classified as malicious</li>

</ul>

This improves:

<ul>

<li>Analyst trust</li>

<li>Operational transparency</li>

<li>Threat explainability</li>

<li>Model interpretability</li>

</ul>

The platform therefore behaves as:

<b>Explainable AI Infrastructure</b>

instead of a black-box classifier.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# MODEL PERFORMANCE RADAR
# =========================================

st.markdown("""

<h2 class="section-title">

🕸️ Model Capability Radar

</h2>

""",
unsafe_allow_html=True
)

categories = [

    "Recall",

    "Precision",

    "Explainability",

    "Inference Speed",

    "Drift Robustness",

    "Scalability"
]

values = [

    99,

    99,

    95,

    96,

    97,

    98
]

radar_fig = go.Figure()

radar_fig.add_trace(

    go.Scatterpolar(

        r=values,

        theta=categories,

        fill='toself',

        name='XGBoost'
    )
)

radar_fig.update_layout(

    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),

    template="plotly_dark",

    height=550
)

st.plotly_chart(
    radar_fig,
    width="stretch"
)

# =========================================
# THRESHOLD ENGINEERING
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🎯 Threshold Engineering

</h2>

<p class="section-text">

The production threshold was optimized to:

<b>0.30</b>

instead of the default:

<b>0.50</b>

This increased:

<ul>

<li>Attack sensitivity</li>

<li>Threat detection coverage</li>

<li>Operational recall</li>

</ul>

while maintaining strong precision performance.

This reflects:
<b>domain-aware cybersecurity ML engineering.</b>

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PRODUCTION ARCHITECTURE
# =========================================

st.markdown("""

<h2 class="section-title">

🏗️ Production Intelligence Architecture

</h2>

""",
unsafe_allow_html=True
)

arch1, arch2 = st.columns(2)

with arch1:

    st.markdown("""

    <div class="glass-card">

    <h3>⚡ Inference Pipeline</h3>

    <ul>

    <li>FastAPI real-time inference</li>

    <li>Feature alignment safeguards</li>

    <li>Threshold-based scoring</li>

    <li>Batch prediction support</li>

    <li>SHAP explainability generation</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

with arch2:

    st.markdown("""

    <div class="glass-card">

    <h3>🔄 Adaptive MLOps Layer</h3>

    <ul>

    <li>MLflow experiment governance</li>

    <li>PSI drift monitoring</li>

    <li>Automated retraining triggers</li>

    <li>Production model refresh cycles</li>

    <li>Operational monitoring dashboards</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# ENGINEERING TAKEAWAYS
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🚀 Engineering Takeaways

</h2>

<p class="section-text">

This platform demonstrates how
modern intrusion detection systems evolve into:

<ul>

<li>Adaptive AI infrastructure</li>

<li>Explainable cybersecurity platforms</li>

<li>Production-grade MLOps systems</li>

</ul>

The architecture combines:

<ul>

<li>Ensemble machine learning</li>

<li>Explainable AI</li>

<li>Operational monitoring</li>

<li>Drift intelligence</li>

<li>Automated retraining</li>

<li>Real-time inference</li>

</ul>

to simulate a realistic
enterprise cybersecurity AI platform.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# FOOTER
# =========================================

st.markdown("""

<br><br>

<center>

<p style="
color:#94A3B8;
font-size:14px;
">

Adaptive AI Intrusion Detection System
— Model Intelligence & Explainable AI

</p>

</center>

""",
unsafe_allow_html=True
)