import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Drift Intelligence",
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
# LOAD DATA
# =========================================

df = pd.read_csv(
    r"data\processed\psi_drift_results.csv"
)

# =========================================
# METRICS
# =========================================

max_psi = round(
    df["PSI Score"].max(),
    3
)

significant_drift = (
    df[
        df["Drift Level"]
        == "Significant Drift"
    ]
    .shape[0]
)

moderate_drift = (
    df[
        df["Drift Level"]
        == "Moderate Drift"
    ]
    .shape[0]
)

stable_features = (
    df[
        df["Drift Level"]
        == "No Drift"
    ]
    .shape[0]
)

# =========================================
# HERO SECTION
# =========================================

st.markdown("""

<div class="hero-section">

<h1 class="hero-title">

🌪️ Adaptive Drift Intelligence Center

</h1>

<p class="hero-subtitle">

Real-time monitoring system for
feature distribution shifts,
model stability analysis,
drift severity detection,
and automated retraining intelligence.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# ALERT BANNER
# =========================================

if max_psi > 0.25:

    st.markdown("""

    <div style="
    background: linear-gradient(
        90deg,
        rgba(255,0,80,0.18),
        rgba(255,0,120,0.05)
    );
    border: 1px solid rgba(255,0,80,0.4);
    padding: 20px;
    border-radius: 18px;
    margin-bottom: 25px;
    ">

    <h2 style="
    color:#FF4D6D;
    margin-bottom:10px;
    ">

    ⚠️ Significant Drift Detected

    </h2>

    <p style="
    color:#CBD5E1;
    font-size:16px;
    ">

    Production traffic behavior has deviated
    significantly from training distributions.

    Automated retraining pipelines
    should be triggered to maintain
    model reliability and detection quality.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# TOP METRICS
# =========================================

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:

    st.markdown(f"""

    <div class="metric-card">

    <h3>📈 Max PSI</h3>

    <h1>{max_psi}</h1>

    <p>Highest observed feature drift</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric2:

    st.markdown(f"""

    <div class="metric-card">

    <h3>🚨 Significant Drift</h3>

    <h1>{significant_drift}</h1>

    <p>Features requiring attention</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric3:

    st.markdown(f"""

    <div class="metric-card">

    <h3>⚠️ Moderate Drift</h3>

    <h1>{moderate_drift}</h1>

    <p>Features showing instability</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric4:

    st.markdown(f"""

    <div class="metric-card">

    <h3>✅ Stable Features</h3>

    <h1>{stable_features}</h1>

    <p>Healthy feature distributions</p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# DRIFT VISUALIZATION
# =========================================

st.markdown("""

<h2 class="section-title">

📊 Feature Drift Analysis

</h2>

""",
unsafe_allow_html=True
)

top_drift = (
    df.sort_values(
        "PSI Score",
        ascending=False
    )
    .head(15)
)

color_map = {

    "No Drift":"#00FFB3",

    "Moderate Drift":"#FFD166",

    "Significant Drift":"#FF4D6D"
}

fig = px.bar(

    top_drift,

    x="PSI Score",

    y="Feature",

    orientation="h",

    color="Drift Level",

    color_discrete_map=color_map,

    title="Top Drifted Features"
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
# DRIFT DISTRIBUTION
# =========================================

col1, col2 = st.columns(2)

with col1:

    st.markdown("""

    <h2 class="section-title">

    🧠 Drift Severity Distribution

    </h2>

    """,
    unsafe_allow_html=True
    )

    severity_counts = (
        df["Drift Level"]
        .value_counts()
        .reset_index()
    )

    severity_counts.columns = [
        "Drift Level",
        "Count"
    ]

    pie_fig = px.pie(

        severity_counts,

        names="Drift Level",

        values="Count",

        hole=0.55,

        color="Drift Level",

        color_discrete_map=color_map
    )

    pie_fig.update_layout(

        template="plotly_dark",

        height=450,

        paper_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white"
        )
    )

    st.plotly_chart(
        pie_fig,
        width="stretch"
    )

with col2:

    st.markdown("""

    <h2 class="section-title">

    📖 PSI Severity Interpretation

    </h2>

    """,
    unsafe_allow_html=True
    )

    st.markdown("""

    <div class="glass-card">

    <h3 style="color:#00FFB3;">
    ✅ PSI &lt; 0.10
    </h3>

    <p class="section-text">

    Stable feature behavior.
    No operational action required.

    </p>

    <hr>

    <h3 style="color:#FFD166;">
    ⚠️ PSI 0.10 — 0.25
    </h3>

    <p class="section-text">

    Moderate distribution changes detected.
    Monitor traffic carefully.

    </p>

    <hr>

    <h3 style="color:#FF4D6D;">
    🚨 PSI &gt; 0.25
    </h3>

    <p class="section-text">

    Significant feature drift detected.
    Retraining pipelines recommended.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# TOP DRIFT TABLE
# =========================================

st.markdown("""

<h2 class="section-title">

📋 Top Drifted Features

</h2>

""",
unsafe_allow_html=True
)

styled_df = top_drift.style.background_gradient(
    cmap="RdYlGn_r",
    subset=["PSI Score"]
)

st.dataframe(
    styled_df,
    width="stretch"
)

# =========================================
# OPERATIONAL INSIGHTS
# =========================================

st.markdown("""

<h2 class="section-title">

🧠 Operational Intelligence Insights

</h2>

""",
unsafe_allow_html=True
)

insight1, insight2 = st.columns(2)

with insight1:

    st.markdown("""

    <div class="glass-card">

    <h3>🌐 Why Drift Happens</h3>

    <p class="section-text">

    Network traffic evolves continuously due to:

    <ul>

    <li>Changing user behavior</li>

    <li>Infrastructure modifications</li>

    <li>New attack strategies</li>

    <li>Protocol evolution</li>

    <li>Seasonal traffic patterns</li>

    <li>Emerging malware activity</li>

    </ul>

    Without monitoring,
    model performance gradually degrades.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

with insight2:

    st.markdown("""

    <div class="glass-card">

    <h3>🔄 Adaptive Retraining Logic</h3>

    <p class="section-text">

    When PSI thresholds exceed
    operational safety limits:

    <ul>

    <li>Drift alerts are triggered</li>

    <li>Retraining workflows begin</li>

    <li>Fresh datasets are loaded</li>

    <li>Ensemble benchmarking restarts</li>

    <li>Best models replace production models</li>

    </ul>

    This enables continuous
    adaptive AI evolution.

    </p>

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

Most machine learning systems fail silently
after deployment because production data evolves.

This platform solves that problem using:

<ul>

<li>Population Stability Index monitoring</li>

<li>Feature distribution analysis</li>

<li>Operational drift intelligence</li>

<li>Automated retraining pipelines</li>

<li>Adaptive production model refresh cycles</li>

</ul>

This transforms the platform from:

<ul>

<li>Static machine learning deployment</li>

</ul>

into:

<ul>

<li>Adaptive production-grade MLOps infrastructure</li>

</ul>

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
— Drift Intelligence & Adaptive Monitoring

</p>

</center>

""",
unsafe_allow_html=True
)