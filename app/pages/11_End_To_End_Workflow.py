import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="End-To-End Workflow",
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

🏗️ End-To-End Engineering Workflow

</h1>

<p class="hero-subtitle">

Complete enterprise-grade engineering walkthrough
covering the entire lifecycle
from raw network traffic ingestion
to adaptive production MLOps deployment.

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

    st.metric(
        "Dataset",
        "CICIDS2017"
    )

with metric2:

    st.metric(
        "Features",
        "68"
    )

with metric3:

    st.metric(
        "Models Benchmarked",
        "6"
    )

with metric4:

    st.metric(
        "Production Model",
        "XGBoost"
    )

with metric5:

    st.metric(
        "Architecture",
        "Adaptive MLOps"
    )

# =========================================
# MASTER PIPELINE
# =========================================

st.markdown("""

<h2 class="section-title">

🧠 Full System Lifecycle

</h2>

""",
unsafe_allow_html=True
)

workflow_steps = [

    "Raw Data Collection",

    "Data Cleaning",

    "Feature Engineering",

    "Exploratory Analysis",

    "Class Imbalance Analysis",

    "Ensemble Benchmarking",

    "Hyperparameter Tuning",

    "Threshold Engineering",

    "Final Model Selection",

    "MLflow Experiment Tracking",

    "Model Serialization",

    "FastAPI API Development",

    "Feature Alignment Pipeline",

    "SHAP Explainability",

    "Batch Prediction Pipelines",

    "Drift Monitoring",

    "Automated Retraining",

    "Streamlit Frontend",

    "Live SOC Dashboard",

    "Documentation Platform"
]

workflow_df = pd.DataFrame({

    "Stage":

        list(range(
            1,
            len(workflow_steps)+1
        )),

    "Step":

        workflow_steps
})

fig = px.line(

    workflow_df,

    x="Stage",

    y=[1]*len(workflow_steps),

    text="Step",

    markers=True
)

fig.update_traces(
    textposition="top center"
)

fig.update_layout(

    template="plotly_dark",

    yaxis_visible=False,

    showlegend=False,

    height=550
)

st.plotly_chart(
    fig,
    width="stretch"
)

# =========================================
# PHASE 1
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

📥 Phase 1 — Raw Data Acquisition

</h2>

<p class="section-text">

The project began using the CICIDS2017 dataset,
developed by the Canadian Institute for Cybersecurity.

The dataset was selected because it contains:

<ul>

<li>Realistic enterprise traffic simulations</li>

<li>Modern attack behavior</li>

<li>Flow-based traffic statistics</li>

<li>Packet aggregation metrics</li>

<li>Behavioral network intelligence</li>

</ul>

Attack categories included:

<ul>

<li>DDoS attacks</li>

<li>Port scanning</li>

<li>Brute-force attacks</li>

<li>Botnet traffic</li>

<li>Web attacks</li>

<li>Infiltration attempts</li>

</ul>

This dataset provided
a realistic foundation
for adaptive intrusion detection engineering.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 2
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🧹 Phase 2 — Data Cleaning & Preprocessing

</h2>

<p class="section-text">

Raw cybersecurity datasets contain significant noise
and preprocessing challenges.

Key preprocessing operations included:

<ul>

<li>Merging multiple CSV traffic files</li>

<li>Handling missing values</li>

<li>Replacing infinite values</li>

<li>Removing corrupted records</li>

<li>Dropping incompatible object columns</li>

<li>Feature schema standardization</li>

</ul>

</p>

<h3>Challenges Faced</h3>

<ul>

<li>Infinite values caused by division-based traffic features</li>

<li>Object-type columns incompatible with boosting models</li>

<li>Memory-heavy preprocessing operations</li>

<li>Schema inconsistency across datasets</li>

</ul>

<h3>Resolution Strategy</h3>

<ul>

<li>Infinity replacement pipelines were implemented</li>

<li>Object columns were removed or transformed</li>

<li>Efficient Pandas workflows were optimized</li>

<li>Feature consistency safeguards were created</li>

</ul>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 3
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

📊 Phase 3 — Exploratory Analysis & Domain Understanding

</h2>

<p class="section-text">

Traffic behavior analysis was conducted
to understand:

<ul>

<li>Network traffic distributions</li>

<li>Attack frequency patterns</li>

<li>Traffic burst behavior</li>

<li>Packet variability</li>

<li>Protocol abnormalities</li>

<li>Class imbalance severity</li>

</ul>

This phase identified:

<ul>

<li>Highly predictive behavioral features</li>

<li>Drift-sensitive variables</li>

<li>Traffic anomalies correlated with attacks</li>

<li>Feature engineering opportunities</li>

</ul>

This phase was critical for:
<b>cybersecurity domain understanding.</b>

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 4
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

⚖️ Phase 4 — Class Imbalance Engineering

</h2>

<p class="section-text">

The dataset exhibited heavy class imbalance.

Benign traffic dominated malicious traffic,
creating major ML risks:

<ul>

<li>Artificially inflated accuracy</li>

<li>Biased benign predictions</li>

<li>Reduced attack sensitivity</li>

<li>Operationally dangerous false negatives</li>

</ul>

To address this:

<ul>

<li>Recall became a strategic metric</li>

<li>Threshold engineering was introduced</li>

<li>ROC-AUC monitoring was prioritized</li>

<li>F1 Score validation was added</li>

</ul>

The system was optimized
for threat detection quality
instead of maximizing raw accuracy.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 5
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🤖 Phase 5 — Ensemble Model Benchmarking

</h2>

<p class="section-text">

Instead of selecting a single model immediately,
multiple ensemble architectures were benchmarked.

Models evaluated included:

<ul>

<li>Random Forest</li>

<li>Gradient Boosting</li>

<li>AdaBoost</li>

<li>LightGBM</li>

<li>CatBoost</li>

<li>XGBoost</li>

</ul>

Each model was evaluated using:

<ul>

<li>Accuracy</li>

<li>Precision</li>

<li>Recall</li>

<li>F1 Score</li>

<li>ROC-AUC</li>

<li>Inference latency</li>

<li>Drift robustness</li>

</ul>

</p>

<h3>Key Engineering Challenges</h3>

<ul>

<li>Balancing recall and inference speed</li>

<li>Comparing multiple boosting architectures</li>

<li>Maintaining explainability compatibility</li>

<li>Ensuring production scalability</li>

</ul>

<h3>Resolution Strategy</h3>

<ul>

<li>XGBoost achieved strongest ROC-AUC</li>

<li>XGBoost provided strongest recall</li>

<li>Boosted trees handled tabular traffic effectively</li>

<li>SHAP integration compatibility was strongest with XGBoost</li>

</ul>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 6
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🎯 Phase 6 — Threshold Engineering

</h2>

<p class="section-text">

The default binary classification threshold
of 0.50 was not ideal for intrusion detection.

Cybersecurity systems require higher sensitivity
because false negatives are operationally dangerous.

The production threshold was optimized to:

<b>0.30</b>

This improved:

<ul>

<li>Threat detection sensitivity</li>

<li>Attack recall</li>

<li>Detection coverage</li>

<li>Operational awareness</li>

</ul>

while maintaining strong precision performance.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 7
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

📈 Phase 7 — MLflow Experiment Governance

</h2>

<p class="section-text">

MLflow was integrated to provide:

<ul>

<li>Experiment tracking</li>

<li>Metric logging</li>

<li>Artifact storage</li>

<li>Model versioning</li>

<li>Performance comparison</li>

<li>Reproducible ML workflows</li>

</ul>

This transformed the project from:

<ul>

<li>Notebook experimentation</li>

</ul>

into:

<ul>

<li>Production-grade governed ML infrastructure</li>

</ul>

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 8
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

⚡ Phase 8 — FastAPI Backend Engineering

</h2>

<p class="section-text">

A production inference API was built using FastAPI.

Capabilities included:

<ul>

<li>Real-time prediction APIs</li>

<li>Probability scoring</li>

<li>SHAP explainability</li>

<li>Pydantic validation</li>

<li>Structured JSON inference</li>

<li>Feature alignment safeguards</li>

</ul>

</p>

<h3>Challenges Faced</h3>

<ul>

<li>422 validation errors</li>

<li>Schema mismatch during inference</li>

<li>Feature ordering inconsistencies</li>

<li>Training-serving skew risks</li>

</ul>

<h3>Resolution Strategy</h3>

<ul>

<li>Pydantic schemas were implemented</li>

<li>Feature alignment pipelines were created</li>

<li>Input normalization logic was added</li>

<li>Inference consistency validation was enforced</li>

</ul>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 9
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🔬 Phase 9 — Explainable AI Integration

</h2>

<p class="section-text">

SHAP explainability was integrated
to provide prediction transparency.

The system now explains:

<ul>

<li>Why predictions occurred</li>

<li>Which features influenced attacks</li>

<li>How traffic behavior changed</li>

<li>Which variables contributed most strongly</li>

</ul>

This improved:

<ul>

<li>Analyst trust</li>

<li>Operational transparency</li>

<li>Model interpretability</li>

<li>Prediction explainability</li>

</ul>

This transformed the system
from a black-box classifier
into an explainable AI platform.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 10
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

📦 Phase 10 — Batch Inference Engineering

</h2>

<p class="section-text">

Batch prediction pipelines were created
to process large-scale CSV traffic datasets.

Capabilities included:

<ul>

<li>Bulk prediction workflows</li>

<li>Attack probability scoring</li>

<li>CSV export generation</li>

<li>Large-scale inference handling</li>

<li>Production-style scoring pipelines</li>

</ul>

This enabled scalable offline traffic analysis
for operational workflows.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 11
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🌪️ Phase 11 — Drift Monitoring Architecture

</h2>

<p class="section-text">

Production traffic evolves continuously.

To monitor behavioral distribution changes,
Population Stability Index (PSI)
was implemented.

The platform compares:

<ul>

<li>Training feature distributions</li>

<li>Production feature distributions</li>

</ul>

to detect:

<ul>

<li>Data drift</li>

<li>Behavioral instability</li>

<li>Feature distribution shifts</li>

<li>Potential model degradation</li>

</ul>

</p>

<h3>Challenges Faced</h3>

<ul>

<li>Defining safe drift thresholds</li>

<li>Balancing sensitivity and false alarms</li>

<li>Monitoring high-dimensional feature behavior</li>

</ul>

<h3>Resolution Strategy</h3>

<ul>

<li>PSI thresholds were standardized</li>

<li>Drift severity categories were introduced</li>

<li>Automated retraining triggers were connected</li>

</ul>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 12
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🔄 Phase 12 — Automated Retraining System

</h2>

<p class="section-text">

When drift exceeded safe operational thresholds,
the system automatically triggered retraining workflows.

The retraining pipeline performs:

<ul>

<li>Fresh dataset loading</li>

<li>Preprocessing validation</li>

<li>Ensemble benchmarking</li>

<li>Evaluation comparison</li>

<li>Best model selection</li>

<li>MLflow logging</li>

<li>Production model replacement</li>

</ul>

This enables:

<ul>

<li>Continuous adaptation</li>

<li>Model freshness</li>

<li>Operational stability</li>

<li>Long-term scalability</li>

</ul>

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PHASE 13
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🖥️ Phase 13 — Frontend & Visualization Engineering

</h2>

<p class="section-text">

A production-style monitoring dashboard
was developed using Streamlit.

The frontend platform includes:

<ul>

<li>Real-time prediction dashboards</li>

<li>Batch upload interfaces</li>

<li>SHAP visualizations</li>

<li>Drift dashboards</li>

<li>Live SOC simulations</li>

<li>Engineering documentation portals</li>

</ul>

</p>

<h3>Challenges Faced</h3>

<ul>

<li>Maintaining visual consistency</li>

<li>Managing multi-page architecture</li>

<li>Handling dynamic UI rendering</li>

<li>Creating enterprise-grade aesthetics</li>

</ul>

<h3>Resolution Strategy</h3>

<ul>

<li>Custom CSS architecture was implemented</li>

<li>Glassmorphism UI design was standardized</li>

<li>Reusable dashboard components were created</li>

<li>Interactive Plotly visualizations were integrated</li>

</ul>

</div>

""",
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

This project evolved from:

<ul>

<li>Offline ML experimentation</li>

</ul>

into:

<ul>

<li>Adaptive production-grade MLOps infrastructure</li>

</ul>

The final system integrates:

<ul>

<li>Ensemble Machine Learning</li>

<li>Production APIs</li>

<li>Explainable AI</li>

<li>Drift Monitoring</li>

<li>Automated Retraining</li>

<li>MLflow Governance</li>

<li>Operational Dashboards</li>

<li>Enterprise Visualization</li>

<li>Production Inference Pipelines</li>

<li>Adaptive Monitoring Systems</li>

</ul>

to simulate a realistic
AI-powered cybersecurity platform.

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
— Enterprise Engineering Lifecycle Documentation

</p>

</center>

""",
unsafe_allow_html=True
)