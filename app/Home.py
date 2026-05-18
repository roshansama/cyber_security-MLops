import streamlit as st


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Adaptive IDS Platform",
    page_icon="🛡️",
    layout="wide"
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
# HERO SECTION
# =====================================

st.title(
    "🛡️ Adaptive Intrusion Detection System"
)

st.subheader(
    "Drift-Aware Explainable Cybersecurity Platform"
)


# =====================================
# OVERVIEW
# =====================================

st.markdown("""

This platform delivers an enterprise-grade intrusion detection pipeline powered by:

- Explainable Machine Learning
- Drift-Aware Monitoring
- Adaptive Retraining
- Real-Time Prediction APIs
- Production MLOps Infrastructure

The system is designed to detect malicious network traffic while continuously monitoring distribution drift and maintaining operational robustness under changing traffic conditions.

""")


# =====================================
# PLATFORM CAPABILITIES
# =====================================

st.header(
    "⚙️ Platform Capabilities"
)

col1, col2 = st.columns(2)


with col1:

    st.markdown("""

### 🤖 Machine Learning

- XGBoost IDS Engine
- Hyperparameter Tuning
- Temporal Validation
- Drift Robustness Testing
- Imbalance-Aware Training
- Explainable AI with SHAP

""")


with col2:

    st.markdown("""

### 🚀 MLOps Infrastructure

- MLflow Experiment Tracking
- FastAPI Model Serving
- Drift Monitoring Pipeline
- Retraining Trigger System
- Production Inference APIs
- Real-Time Explainability

""")


# =====================================
# SYSTEM WORKFLOW
# =====================================

st.header(
    "🔄 System Workflow"
)

workflow = """
Raw Traffic Data
        ↓
Data Cleaning & Validation
        ↓
Feature Engineering
        ↓
Model Training
        ↓
Hyperparameter Tuning
        ↓
Drift Robustness Evaluation
        ↓
FastAPI Inference Layer
        ↓
SHAP Explainability
        ↓
Drift Monitoring
        ↓
Automated Retraining Trigger
"""

st.code(
    workflow,
    language="text"
)


# =====================================
# MODEL PERFORMANCE
# =====================================

st.header(
    "📊 Model Performance Snapshot"
)

metric1, metric2, metric3 = st.columns(3)


with metric1:

    st.metric(
        label="ROC-AUC",
        value="0.9999"
    )


with metric2:

    st.metric(
        label="F1 Score",
        value="0.9974"
    )


with metric3:

    st.metric(
        label="Detection Accuracy",
        value="99.91%"
    )


# =====================================
# DRIFT INTELLIGENCE
# =====================================

st.header(
    "📈 Drift Intelligence"
)

st.markdown("""

The platform continuously monitors:

- Feature distribution instability
- PSI drift thresholds
- Temporal degradation
- Prediction confidence changes
- Retraining requirements

Drift-aware retraining logic ensures the IDS remains adaptive against evolving traffic behavior.

""")


# =====================================
# EXPLAINABILITY
# =====================================

st.header(
    "🔬 Explainable AI"
)

st.markdown("""

Each prediction includes:

- SHAP feature attribution
- Feature contribution ranking
- Prediction confidence scoring
- Transparent decision reasoning

This enables cybersecurity analysts to understand *why* a prediction was generated rather than treating the model as a black box.

""")


# =====================================
# FOOTER
# =====================================

st.markdown("---")

st.caption(
    "Adaptive IDS Platform | MLOps + Explainable Cybersecurity + Drift Intelligence"
)