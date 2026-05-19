import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Model Pipeline",
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

🧠 Adaptive AI Model Pipeline

</h1>

<p class="hero-subtitle">

Complete production-grade engineering walkthrough
covering ensemble benchmarking,
threshold engineering,
explainable AI,
deployment architecture,
and adaptive MLOps workflows.

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
        "Production Model",
        "XGBoost"
    )

with metric2:

    st.metric(
        "Models Benchmarked",
        "6"
    )

with metric3:

    st.metric(
        "Recall",
        "99.83%"
    )

with metric4:

    st.metric(
        "ROC-AUC",
        "0.9999"
    )

with metric5:

    st.metric(
        "Threshold",
        "0.30"
    )

# =========================================
# PIPELINE OVERVIEW
# =========================================

st.markdown("""

<h2 class="section-title">

🏗️ End-To-End ML Pipeline

</h2>

""",
unsafe_allow_html=True
)

pipeline_steps = [

    "Raw Data Loading",

    "Data Cleaning",

    "Feature Engineering",

    "EDA & Traffic Analysis",

    "Class Imbalance Investigation",

    "Train/Test Split",

    "Multi-Model Benchmarking",

    "Hyperparameter Tuning",

    "Threshold Optimization",

    "Best Model Selection",

    "MLflow Logging",

    "Model Serialization",

    "FastAPI Deployment",

    "Feature Alignment",

    "SHAP Explainability",

    "Drift Monitoring",

    "Automated Retraining"
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

fig = px.line(

    pipeline_df,

    x="Stage",

    y=[1]*len(pipeline_steps),

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

    height=500
)

st.plotly_chart(
    fig,
    width="stretch"
)

# =========================================
# WHY MACHINE LEARNING
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🤖 Why Machine Learning For Intrusion Detection?

</h2>

<p class="section-text">

Traditional intrusion detection systems rely heavily on:

<ul>

<li>Static attack signatures</li>

<li>Manual rules</li>

<li>Predefined threat definitions</li>

</ul>

These systems struggle against:

<ul>

<li>Zero-day attacks</li>

<li>Behavioral anomalies</li>

<li>Evolving attacker strategies</li>

<li>Large-scale traffic analysis</li>

</ul>

Machine learning enables the system to:

<ul>

<li>Learn hidden traffic behavior patterns</li>

<li>Detect statistical anomalies</li>

<li>Adapt to evolving traffic distributions</li>

<li>Generalize across unseen attacks</li>

<li>Improve operational scalability</li>

</ul>

This transforms intrusion detection
from static rule processing
into adaptive behavioral intelligence.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# ENSEMBLE BENCHMARKING
# =========================================

st.markdown("""

<h2 class="section-title">

📊 Ensemble Model Benchmarking

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

    "Precision":[

        0.995,
        0.991,
        0.985,
        0.997,
        0.996,
        0.997
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

Multiple ensemble architectures were benchmarked
before selecting the final production model.

XGBoost achieved the strongest balance between:

<ul>

<li>Recall</li>

<li>ROC-AUC</li>

<li>Inference latency</li>

<li>Drift robustness</li>

<li>Production scalability</li>

<li>SHAP explainability compatibility</li>

</ul>

XGBoost was particularly effective because:

<ul>

<li>Tree boosting captures non-linear traffic behavior</li>

<li>Ensemble learning improves robustness</li>

<li>Gradient optimization improves attack separation</li>

<li>Tabular cybersecurity data strongly favors boosted trees</li>

</ul>

The final production decision prioritized:

<ul>

<li>Threat detection sensitivity</li>

<li>Operational reliability</li>

<li>Explainability</li>

<li>Scalable inference performance</li>

</ul>

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# WHY NOT DEEP LEARNING
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🧩 Why Deep Learning Was Not Selected

</h2>

<p class="section-text">

Although deep learning is powerful,
tabular intrusion detection datasets often favor
ensemble boosting architectures.

Compared to deep learning,
XGBoost and boosting ensembles provided:

<ul>

<li>Lower computational cost</li>

<li>Faster inference speed</li>

<li>Simpler deployment</li>

<li>Better explainability</li>

<li>Stronger tabular performance</li>

<li>Reduced infrastructure complexity</li>

</ul>

For this project,
production engineering simplicity
and operational explainability
were prioritized heavily.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# THRESHOLD ENGINEERING
# =========================================

st.markdown("""

<h2 class="section-title">

🎯 Threshold Engineering

</h2>

""",
unsafe_allow_html=True
)

th1, th2 = st.columns(2)

with th1:

    st.markdown("""

    <div class="glass-card">

    <h3>Default Classification Threshold</h3>

    <p class="section-text">

    Most ML systems use a default threshold of:

    <b>0.50</b>

    However,
    cybersecurity systems have asymmetric risk.

    Missing attacks is operationally more dangerous
    than generating false positives.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

with th2:

    st.markdown("""

    <div class="glass-card">

    <h3>Optimized Production Threshold</h3>

    <p class="section-text">

    The production threshold was optimized to:

    <b>0.30</b>

    This improved:

    <ul>

    <li>Attack recall</li>

    <li>Threat sensitivity</li>

    <li>Detection coverage</li>

    </ul>

    while maintaining strong precision performance.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# CLASS IMBALANCE
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

⚖️ Class Imbalance Engineering

</h2>

<p class="section-text">

Intrusion detection datasets are naturally imbalanced.

Benign traffic heavily dominates malicious traffic.

This creates several ML challenges:

<ul>

<li>Artificially inflated accuracy</li>

<li>Biased benign predictions</li>

<li>Dangerous false negatives</li>

<li>Poor attack sensitivity</li>

</ul>

To address this:

<ul>

<li>Recall was prioritized strategically</li>

<li>Threshold optimization was implemented</li>

<li>ROC-AUC monitoring was added</li>

<li>Drift robustness evaluation was conducted</li>

</ul>

This ensured the system focused on
threat detection quality
instead of only maximizing accuracy.

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

Cybersecurity analysts require visibility into:

<ul>

<li>Why predictions occurred</li>

<li>Which features influenced attacks</li>

<li>How traffic behavior changed</li>

</ul>

SHAP (SHapley Additive Explanations)
was integrated to provide:

<ul>

<li>Local prediction explanations</li>

<li>Feature attribution analysis</li>

<li>Transparent model reasoning</li>

<li>Operational analyst trust</li>

</ul>

This transformed the platform
from a black-box classifier
into an explainable AI system.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# FEATURE ALIGNMENT
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🧩 Feature Alignment Pipeline

</h2>

<p class="section-text">

Production inference systems commonly fail due to:

<ul>

<li>Missing features</li>

<li>Incorrect column ordering</li>

<li>Schema inconsistencies</li>

<li>Training-serving skew</li>

</ul>

To solve this,
a dedicated feature alignment pipeline
was implemented.

This guarantees:

<ul>

<li>Stable inference schema</li>

<li>Consistent model inputs</li>

<li>Reliable API predictions</li>

<li>Production inference stability</li>

</ul>

This became a critical production engineering safeguard.

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

    <li>Large-scale dataset processing</li>

    <li>Class imbalance</li>

    <li>Infinite feature values</li>

    <li>Schema mismatches</li>

    <li>Object columns in XGBoost</li>

    <li>Inference consistency issues</li>

    <li>Production drift risks</li>

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

    <li>Custom preprocessing pipelines</li>

    <li>Threshold engineering</li>

    <li>Feature alignment safeguards</li>

    <li>PSI drift monitoring</li>

    <li>Automated retraining</li>

    <li>MLflow governance workflows</li>

    <li>SHAP explainability integration</li>

    </ul>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# MLFLOW
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

📈 MLflow Experiment Governance

</h2>

<p class="section-text">

MLflow was integrated to provide:

<ul>

<li>Experiment tracking</li>

<li>Metric logging</li>

<li>Artifact storage</li>

<li>Model lineage</li>

<li>Version comparison</li>

<li>Reproducible ML workflows</li>

</ul>

This transformed the project
from notebook experimentation
into governed production ML infrastructure.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# DRIFT & RETRAINING
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🔄 Adaptive Drift Monitoring & Retraining

</h2>

<p class="section-text">

Network traffic evolves continuously.

This creates:

<b>Data Drift</b>

To address this,
the platform implements:

<ul>

<li>Population Stability Index (PSI)</li>

<li>Feature distribution monitoring</li>

<li>Drift severity thresholds</li>

<li>Automated retraining triggers</li>

<li>Production model replacement</li>

</ul>

This enables the system
to behave as adaptive AI infrastructure
instead of a static deployed model.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# FINAL ENGINEERING TAKEAWAYS
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🚀 Final Engineering Takeaways

</h2>

<p class="section-text">

This platform demonstrates how modern
machine learning systems evolve into
production-grade adaptive MLOps ecosystems.

The final architecture integrates:

<ul>

<li>Ensemble ML benchmarking</li>

<li>Production APIs</li>

<li>Explainable AI</li>

<li>Drift monitoring</li>

<li>Automated retraining</li>

<li>Experiment governance</li>

<li>Operational dashboards</li>

<li>Production inference safeguards</li>

</ul>

to simulate a realistic
AI-powered intrusion detection platform.

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
— Production ML Engineering Architecture

</p>

</center>

""",
unsafe_allow_html=True
)