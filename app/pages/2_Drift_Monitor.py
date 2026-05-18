import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# =====================================
# TITLE
# =====================================

st.title(
    "📈 Drift Monitoring Dashboard"
)


# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv(
    r"D:\MLOPS\data\processed\psi_drift_results.csv"
)


# =====================================
# DISPLAY TABLE
# =====================================

st.subheader(
    "Top Drifted Features"
)

st.dataframe(
    df.head(15)
)


# =====================================
# VISUALIZATION
# =====================================

top_drift = df.head(10)


fig, ax = plt.subplots(
    figsize=(10, 6)
)

ax.barh(
    top_drift["Feature"],
    top_drift["PSI Score"]
)

ax.set_xlabel(
    "PSI Score"
)

ax.set_title(
    "Top Drifted Features"
)

ax.invert_yaxis()

st.pyplot(fig)


# =====================================
# DRIFT SUMMARY
# =====================================

significant_drift = (
    df[
        df["Drift Level"]
        == "Significant Drift"
    ]
    .shape[0]
)


st.metric(
    "Significant Drifted Features",
    significant_drift
)