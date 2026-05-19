import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Drift & Retraining",
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

🔄 Drift Monitoring & Automated Retraining

</h1>

<p class="hero-subtitle">

Production-grade adaptive MLOps architecture
for monitoring changing traffic behavior,
detecting feature drift,
and automatically refreshing production models.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# WHY DRIFT MATTERS
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🌪️ Why Data Drift Matters

</h2>

<p class="section-text">

Machine learning models assume that
future production data will behave similarly
to training data.

In real-world systems,
this assumption eventually breaks.

This phenomenon is called:

<b>Data Drift</b>

In cybersecurity environments,
network traffic evolves continuously due to:

<ul>

<li>Changing user behavior</li>

<li>New attack strategies</li>

<li>Infrastructure modifications</li>

<li>Protocol evolution</li>

<li>Traffic seasonality</li>

<li>Emerging malware techniques</li>

</ul>

Without drift monitoring,
model performance gradually degrades over time.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# TYPES OF DRIFT
# =========================================

st.markdown("""

<h2 class="section-title">

🧠 Types Of Drift

</h2>

""",
unsafe_allow_html=True
)

drift1, drift2, drift3 = st.columns(3)

with drift1:

    st.markdown("""

    <div class="glass-card">

    <h3>Data Drift</h3>

    <p class="section-text">

    Feature distributions change over time.

    Example:
    packet rates become significantly different
    from training behavior.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

with drift2:

    st.markdown("""

    <div class="glass-card">

    <h3>Concept Drift</h3>

    <p class="section-text">

    The relationship between features
    and attack labels changes over time.

    Example:
    attackers evolve tactics.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

with drift3:

    st.markdown("""

    <div class="glass-card">

    <h3>Prediction Drift</h3>

    <p class="section-text">

    Model predictions become unstable
    due to changing production patterns.

    Example:
    increasing false positives.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# PSI EXPLANATION
# =========================================

st.markdown("""

<h2 class="section-title">

📊 Population Stability Index (PSI)

</h2>

""",
unsafe_allow_html=True
)

st.markdown("""

<div class="glass-card">

<p class="section-text">

The project uses:

<b>Population Stability Index (PSI)</b>

to measure distribution changes between:

<ul>

<li>Training data</li>

<li>Production inference data</li>

</ul>

PSI helps quantify
how much feature behavior has shifted over time.

Higher PSI values indicate stronger drift.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PSI THRESHOLDS
# =========================================

psi_df = pd.DataFrame({

    "PSI Range":[

        "< 0.10",

        "0.10 - 0.25",

        "> 0.25"
    ],

    "Interpretation":[

        "Stable Distribution",

        "Moderate Drift",

        "Significant Drift"
    ],

    "Recommended Action":[

        "Continue Monitoring",

        "Investigate Feature Changes",

        "Trigger Retraining Pipeline"
    ]
})

st.dataframe(
    psi_df,
    width="stretch"
)

# =========================================
# DRIFT VISUALIZATION
# =========================================

st.markdown("""

<h2 class="section-title">

📈 Drift Monitoring Visualization

</h2>

""",
unsafe_allow_html=True
)

drift_df = pd.DataFrame({

    "Feature":[

        "Flow Duration",

        "Packet Length Mean",

        "Flow Bytes/s",

        "Total Fwd Packets",

        "Average Packet Size"
    ],

    "PSI":[

        0.05,
        0.12,
        0.18,
        0.29,
        0.34
    ]
})

drift_fig = px.bar(

    drift_df,

    x="Feature",

    y="PSI",

    color="PSI",

    title="Feature Drift Analysis"
)

drift_fig.update_layout(

    template="plotly_dark",

    height=450
)

st.plotly_chart(
    drift_fig,
    width="stretch"
)

# =========================================
# AUTOMATED RETRAINING
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

⚙️ Automated Retraining Workflow

</h2>

<p class="section-text">

When PSI thresholds exceed acceptable limits,
the platform automatically triggers
a retraining workflow.

The retraining pipeline performs:

<ul>

<li>Fresh dataset loading</li>

<li>Feature preprocessing</li>

<li>Multi-model benchmarking</li>

<li>Model evaluation</li>

<li>Best model selection</li>

<li>MLflow experiment logging</li>

<li>Production model replacement</li>

</ul>

This transforms the system into:

<b>Adaptive AI Infrastructure</b>

instead of a static deployed model.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# RETRAINING PIPELINE
# =========================================

st.markdown("""

<h2 class="section-title">

🔄 Retraining Pipeline Architecture

</h2>

""",
unsafe_allow_html=True
)

pipeline_steps = [

    "Production Data Monitoring",

    "PSI Calculation",

    "Threshold Validation",

    "Drift Detection",

    "Retraining Trigger",

    "Fresh Data Loading",

    "Model Benchmarking",

    "Best Model Selection",

    "MLflow Logging",

    "Production Model Update"
]

pipeline_df = pd.DataFrame({

    "Stage":

        list(range(
            1,
            len(pipeline_steps)+1
        )),

    "Step":

        pipeline_steps
})

pipeline_fig = px.line(

    pipeline_df,

    x="Stage",

    y=[1]*len(pipeline_steps),

    text="Step",

    markers=True
)

pipeline_fig.update_traces(
    textposition="top center"
)

pipeline_fig.update_layout(

    template="plotly_dark",

    yaxis_visible=False,

    showlegend=False,

    height=400
)

st.plotly_chart(
    pipeline_fig,
    width="stretch"
)

# =========================================
# WHY AUTOMATED RETRAINING MATTERS
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🚀 Why Automated Retraining Is Important

</h2>

<p class="section-text">

Static machine learning systems degrade over time.

In cybersecurity,
attack behavior evolves rapidly.

Without retraining:

<ul>

<li>Detection quality decreases</li>

<li>False negatives increase</li>

<li>Threat coverage weakens</li>

<li>Operational trust declines</li>

</ul>

Automated retraining enables:

<ul>

<li>Continuous adaptation</li>

<li>Model freshness</li>

<li>Improved generalization</li>

<li>Long-term production stability</li>

<li>Operational scalability</li>

</ul>

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# MLFLOW INTEGRATION
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

📈 MLflow Integration During Retraining

</h2>

<p class="section-text">

Every retraining cycle is tracked using MLflow.

This provides:

<ul>

<li>Experiment history</li>

<li>Metric comparison</li>

<li>Model lineage</li>

<li>Artifact versioning</li>

<li>Performance auditing</li>

</ul>

This creates reproducible
and production-grade ML governance workflows.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# ENGINEERING INSIGHTS
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🧩 Engineering Insights

</h2>

<p class="section-text">

Most machine learning portfolio projects
focus only on training accuracy.

Real-world ML systems must additionally handle:

<ul>

<li>Production monitoring</li>

<li>Distribution changes</li>

<li>Model degradation</li>

<li>Data evolution</li>

<li>Operational automation</li>

</ul>

This project demonstrates
how adaptive MLOps systems can continuously:

<ul>

<li>Monitor production health</li>

<li>Detect drift</li>

<li>Refresh models</li>

<li>Maintain detection quality</li>

</ul>

under changing real-world conditions.

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
— Drift Monitoring & Adaptive Retraining

</p>

</center>

""",
unsafe_allow_html=True
)