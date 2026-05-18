import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# =====================================
# TITLE
# =====================================

st.title(
    "🔬 Model Insights Dashboard"
)


# =====================================
# MODEL METRICS
# =====================================

st.header(
    "📊 Performance Metrics"
)

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "ROC-AUC",
        "0.9999"
    )


with col2:

    st.metric(
        "F1 Score",
        "0.9974"
    )


with col3:

    st.metric(
        "Accuracy",
        "99.91%"
    )


# =====================================
# FEATURE IMPORTANCE
# =====================================

st.header(
    "📌 Feature Importance"
)


feature_data = {

    "Feature": [

        "Bwd Packet Length Std",

        "Packet Length Std",

        "Average Packet Size",

        "Destination Port",

        "Init_Win_bytes_forward"
    ],

    "Importance": [

        0.096,

        0.078,

        0.044,

        0.033,

        0.028
    ]
}


df = pd.DataFrame(
    feature_data
)


fig, ax = plt.subplots(
    figsize=(10, 5)
)

ax.barh(
    df["Feature"],
    df["Importance"]
)

ax.set_xlabel(
    "Importance Score"
)

ax.set_title(
    "Top Model Features"
)

ax.invert_yaxis()

st.pyplot(fig)


# =====================================
# MODEL INFORMATION
# =====================================

st.header(
    "🧠 Model Architecture"
)

st.markdown("""

Current Production Model:

- XGBoost Classifier
- Drift Robustness Enhanced
- SHAP Explainability Enabled
- FastAPI Integrated
- MLflow Tracked
- Threshold Optimized

""")