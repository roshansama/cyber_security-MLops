import streamlit as st
import pandas as pd
import plotly.express as px
import random

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Project Overview",
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

<div class="hero-section cyber-grid">

<div class="glow-orb glow-cyan"></div>

<div class="glow-orb glow-pink"></div>

<h1 class="hero-title">

🛡️ Adaptive AI Intrusion Defense Platform

</h1>

<p class="hero-subtitle">

Enterprise-grade adaptive cybersecurity ecosystem
powered by ensemble machine learning,
real-time threat intelligence,
explainable AI,
drift monitoring,
and autonomous retraining infrastructure.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# EXECUTIVE BANNER
# =========================================

st.markdown("""

<div class="glass-card live-alert">

<h2 style="
color:#00E5FF;
margin-bottom:15px;
">

🚀 Enterprise Adaptive AI Infrastructure

</h2>

<p class="section-text">

This platform simulates a real-world
production-grade cybersecurity AI ecosystem
capable of:

<ul>

<li>Real-time attack detection</li>

<li>Adaptive retraining</li>

<li>Drift intelligence monitoring</li>

<li>Explainable AI inference</li>

<li>Operational SOC visualization</li>

<li>Enterprise-scale batch prediction</li>

</ul>

The project was engineered to demonstrate:
<b>practical production MLOps architecture</b>
instead of isolated notebook experimentation.

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

    <h3>🏆 Production Model</h3>

    <h1>XGBoost</h1>

    <p>Final ensemble architecture</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric2:

    st.markdown("""

    <div class="metric-card">

    <h3>📈 ROC-AUC</h3>

    <h1>0.9999</h1>

    <p>Attack separation quality</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric3:

    st.markdown("""

    <div class="metric-card">

    <h3>🚨 Recall</h3>

    <h1>99.83%</h1>

    <p>Threat detection sensitivity</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric4:

    st.markdown("""

    <div class="metric-card">

    <h3>🧠 Models Benchmarked</h3>

    <h1>6</h1>

    <p>Ensemble architectures tested</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric5:

    st.markdown("""

    <div class="metric-card">

    <h3>📡 Features</h3>

    <h1>68</h1>

    <p>Traffic intelligence variables</p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# PLATFORM CAPABILITIES
# =========================================

st.markdown("""

<h2 class="section-title">

🏭 Enterprise AI Capabilities

</h2>

""",
unsafe_allow_html=True
)

cap1, cap2, cap3 = st.columns(3)

with cap1:

    st.markdown("""

    <div class="glass-card">

    <h3>⚡ Real-Time Inference</h3>

    <ul>

    <li>FastAPI prediction APIs</li>

    <li>Low-latency scoring</li>

    <li>Live SOC monitoring</li>

    <li>Threat classification</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

with cap2:

    st.markdown("""

    <div class="glass-card">

    <h3>🌪️ Adaptive MLOps</h3>

    <ul>

    <li>PSI drift monitoring</li>

    <li>Automated retraining</li>

    <li>MLflow governance</li>

    <li>Model lifecycle management</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

with cap3:

    st.markdown("""

    <div class="glass-card">

    <h3>🔬 Explainable AI</h3>

    <ul>

    <li>SHAP explainability</li>

    <li>Feature attribution</li>

    <li>Transparent inference</li>

    <li>Operational analyst trust</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# PROJECT OBJECTIVE
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🎯 Project Objective

</h2>

<p class="section-text">

The primary objective of this project
was to engineer a realistic
adaptive AI intrusion detection platform
that simulates how enterprise cybersecurity
systems operate in production environments.

Unlike traditional rule-based systems,
this platform uses ensemble machine learning
to identify statistical anomalies
inside network traffic flows.

The architecture was designed to solve:

<ul>

<li>Large-scale network traffic analysis</li>

<li>Real-time attack detection</li>

<li>Adaptive model degradation</li>

<li>Operational explainability</li>

<li>Production inference stability</li>

<li>Continuous model evolution</li>

</ul>

The platform therefore behaves as:

<b>adaptive cybersecurity infrastructure</b>

instead of a static deployed classifier.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# TECHNOLOGY STACK
# =========================================

st.markdown("""

<h2 class="section-title">

⚙️ Technology Stack

</h2>

""",
unsafe_allow_html=True
)

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:

    st.markdown("""

    <div class="glass-card">

    <h3>🖥️ Frontend</h3>

    <ul>

    <li>Streamlit</li>

    <li>Plotly</li>

    <li>PyDeck</li>

    <li>Glassmorphism UI</li>

    <li>Custom CSS</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

with tech2:

    st.markdown("""

    <div class="glass-card">

    <h3>⚡ Backend</h3>

    <ul>

    <li>FastAPI</li>

    <li>Uvicorn</li>

    <li>Pydantic</li>

    <li>REST APIs</li>

    <li>JSON inference</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

with tech3:

    st.markdown("""

    <div class="glass-card">

    <h3>🧠 Machine Learning</h3>

    <ul>

    <li>Random Forest</li>

    <li>Gradient Boosting</li>

    <li>AdaBoost</li>

    <li>LightGBM</li>

    <li>CatBoost</li>

    <li>XGBoost</li>

    <li>SHAP Explainability</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

with tech4:

    st.markdown("""

    <div class="glass-card">

    <h3>🔄 MLOps Infrastructure</h3>

    <ul>

    <li>MLflow Tracking</li>

    <li>Drift Monitoring</li>

    <li>Automated Retraining</li>

    <li>Feature Alignment</li>

    <li>Batch Inference</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# SYSTEM ARCHITECTURE
# =========================================

st.markdown("""

<h2 class="section-title">

🏗️ End-To-End System Architecture

</h2>

""",
unsafe_allow_html=True
)

architecture_steps = [

    "Raw Traffic",

    "Cleaning",

    "EDA",

    "Benchmarking",

    "XGBoost",

    "FastAPI",

    "SHAP",

    "Drift Monitoring",

    "Retraining",

    "SOC Dashboard"
]

arch_df = pd.DataFrame({

    "Stage":
        list(range(
            1,
            len(architecture_steps)+1
        )),

    "Step":
        architecture_steps
})

fig = px.line(

    arch_df,

    x="Stage",

    y=[1]*len(architecture_steps),

    text="Step",

    markers=True
)

fig.update_traces(

    textposition="top center",

    line=dict(
        width=5
    ),

    marker=dict(
        size=14
    )
)

fig.update_layout(

    template="plotly_dark",

    showlegend=False,

    yaxis_visible=False,

    height=500,

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font=dict(
        color="white"
    )
)

st.plotly_chart(
    fig,
    width="stretch"
)

# =========================================
# MODEL BENCHMARKING
# =========================================

st.markdown("""

<h2 class="section-title">

📊 Ensemble Benchmarking Intelligence

</h2>

""",
unsafe_allow_html=True
)

benchmark_df = pd.DataFrame({

    "Model":[

        "Random Forest",

        "Gradient Boosting",

        "AdaBoost",

        "LightGBM",

        "CatBoost",

        "XGBoost"
    ],

    "Accuracy":[

        0.996,
        0.994,
        0.989,
        0.998,
        0.998,
        0.999
    ],

    "Recall":[

        0.992,
        0.988,
        0.981,
        0.997,
        0.997,
        0.998
    ],

    "ROC-AUC":[

        0.997,
        0.994,
        0.989,
        0.999,
        0.998,
        0.9999
    ]
})

st.dataframe(
    benchmark_df,
    width="stretch"
)

# =========================================
# WHY XGBOOST WON
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🏆 Why XGBoost Became The Production Model

</h2>

<p class="section-text">

Multiple ensemble architectures
were benchmarked before selecting
the final production model.

XGBoost achieved the strongest balance between:

<ul>

<li>Recall</li>

<li>ROC-AUC</li>

<li>Inference speed</li>

<li>Drift robustness</li>

<li>Production scalability</li>

<li>Explainability compatibility</li>

</ul>

The final optimization strategy prioritized:

<b>threat detection sensitivity</b>

because false negatives are operationally dangerous
in cybersecurity environments.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# ENGINEERING CHALLENGES
# =========================================

st.markdown("""

<h2 class="section-title">

⚠️ Engineering Challenges & Resolutions

</h2>

""",
unsafe_allow_html=True
)

eng1, eng2 = st.columns(2)

with eng1:

    st.markdown("""

    <div class="glass-card">

    <h3>Challenges Faced</h3>

    <ul>

    <li>Class imbalance</li>

    <li>Infinite feature values</li>

    <li>Schema mismatches</li>

    <li>Drift instability</li>

    <li>Inference consistency issues</li>

    <li>Operational explainability</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

with eng2:

    st.markdown("""

    <div class="glass-card">

    <h3>Resolution Strategy</h3>

    <ul>

    <li>Threshold engineering</li>

    <li>Feature alignment safeguards</li>

    <li>PSI drift monitoring</li>

    <li>SHAP explainability</li>

    <li>Automated retraining</li>

    <li>MLflow experiment governance</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# LIVE ENGINEERING TERMINAL
# =========================================

st.markdown("""

<h2 class="section-title">

🖥️ Live Engineering Runtime

</h2>

""",
unsafe_allow_html=True
)

terminal_logs = [

    "[INFO] MLflow tracking active",

    "[INFO] FastAPI inference operational",

    "[WARNING] PSI threshold exceeded",

    "[INFO] Ensemble benchmarking complete",

    "[ALERT] Adaptive retraining triggered",

    "[INFO] SHAP explainability generated",

    "[INFO] Threat scoring completed",

    "[INFO] Drift monitoring synchronized"
]

terminal_html = """

<div class="terminal-window">

<div class="terminal-header">

<div class="terminal-dot term-red"></div>

<div class="terminal-dot term-yellow"></div>

<div class="terminal-dot term-green"></div>

</div>

"""

for log in random.sample(
    terminal_logs,
    6
):

    if "ALERT" in log:

        log_class = "log-alert"

    elif "WARNING" in log:

        log_class = "log-warning"

    else:

        log_class = "log-success"

    terminal_html += f"""

<div class="terminal-log {log_class}">

&gt; {log}

</div>

"""

terminal_html += "</div>"

st.markdown(
    terminal_html,
    unsafe_allow_html=True
)

# =========================================
# FINAL TAKEAWAYS
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🚀 Final Engineering Takeaways

</h2>

<p class="section-text">

This project demonstrates how modern
machine learning systems evolve into:

<ul>

<li>Adaptive AI infrastructure</li>

<li>Production-grade MLOps ecosystems</li>

<li>Explainable cybersecurity platforms</li>

<li>Operational SOC intelligence systems</li>

</ul>

The final architecture integrates:

<ul>

<li>Ensemble machine learning</li>

<li>Real-time APIs</li>

<li>Explainable AI</li>

<li>Drift intelligence</li>

<li>Automated retraining</li>

<li>Enterprise visualization</li>

<li>Production governance</li>

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
— Enterprise Adaptive AI Platform

</p>

</center>

""",
unsafe_allow_html=True
)