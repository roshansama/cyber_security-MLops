import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Batch Threat Analysis",
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

📂 Enterprise Batch Threat Analysis

</h1>

<p class="hero-subtitle">

Production-scale intrusion intelligence platform
for large-volume traffic analysis,
bulk attack detection,
probability scoring,
and operational cybersecurity monitoring.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# INTRODUCTION
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🌐 Batch Inference Architecture

</h2>

<p class="section-text">

The batch inference engine enables
large-scale cybersecurity traffic analysis
using the production XGBoost intrusion detection model.

Capabilities include:

<ul>

<li>Bulk CSV traffic ingestion</li>

<li>Large-scale attack detection</li>

<li>Probability-based threat scoring</li>

<li>Operational traffic monitoring</li>

<li>Batch explainability workflows</li>

<li>Production inference pipelines</li>

</ul>

This simulates realistic enterprise SOC workflows
where millions of traffic flows
must be analyzed continuously.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# FILE UPLOAD SECTION
# =========================================

st.markdown("""

<h2 class="section-title">

📤 Upload Network Traffic Dataset

</h2>

""",
unsafe_allow_html=True
)

uploaded_file = st.file_uploader(

    "Upload CSV File",

    type=["csv"]
)

# =========================================
# FILE INFO
# =========================================

if uploaded_file is not None:

    st.markdown(f"""

    <div class="glass-card">

    <h3 style="color:#00FFB3;">

    ✅ File Uploaded Successfully

    </h3>

    <p class="section-text">

    Uploaded File:
    <b>{uploaded_file.name}</b>

    The dataset is ready for
    enterprise-scale threat analysis.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

    # =====================================
    # RUN PREDICTION
    # =====================================

    if st.button(
        "🚀 Run Enterprise Threat Analysis"
    ):

        with st.spinner(
            "Running large-scale intrusion intelligence analysis..."
        ):

            files = {

                "file": (

                    uploaded_file.name,

                    uploaded_file,

                    "text/csv"
                )
            }

            response = requests.post(

                "http://127.0.0.1:8000/batch_predict",

                files=files
            )

        # =====================================
        # RESPONSE VALIDATION
        # =====================================

        if response.status_code != 200:

            st.error(
                "Batch prediction failed."
            )

        else:

            result = response.json()

            # =================================
            # TOP METRICS
            # =================================

            st.markdown("""

            <h2 class="section-title">

            📊 Batch Intelligence Summary

            </h2>

            """,
            unsafe_allow_html=True
            )

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.markdown(f"""

                <div class="metric-card">

                <h3>📦 Rows Processed</h3>

                <h1>{result["rows_processed"]}</h1>

                <p>Total traffic records analyzed</p>

                </div>

                """,
                unsafe_allow_html=True
                )

            with col2:

                st.markdown(f"""

                <div class="metric-card">

                <h3>🚨 Detected Attacks</h3>

                <h1>{result["attack_count"]}</h1>

                <p>Malicious traffic identified</p>

                </div>

                """,
                unsafe_allow_html=True
                )

            with col3:

                st.markdown(f"""

                <div class="metric-card">

                <h3>✅ Benign Traffic</h3>

                <h1>{result["benign_count"]}</h1>

                <p>Normal network behavior</p>

                </div>

                """,
                unsafe_allow_html=True
                )

            attack_ratio = round(

                (
                    result["attack_count"]
                    /
                    result["rows_processed"]
                ) * 100,

                2
            )

            with col4:

                st.markdown(f"""

                <div class="metric-card">

                <h3>⚠️ Threat Ratio</h3>

                <h1>{attack_ratio}%</h1>

                <p>Attack prevalence detected</p>

                </div>

                """,
                unsafe_allow_html=True
                )

            # =================================
            # TRAFFIC DISTRIBUTION
            # =================================

            st.markdown("""

            <h2 class="section-title">

            📈 Traffic Classification Intelligence

            </h2>

            """,
            unsafe_allow_html=True
            )

            dist_df = pd.DataFrame({

                "Traffic Type":[

                    "Benign",

                    "Attack"
                ],

                "Count":[

                    result["benign_count"],

                    result["attack_count"]
                ]
            })

            pie_fig = px.pie(

                dist_df,

                names="Traffic Type",

                values="Count",

                hole=0.55,

                color="Traffic Type",

                color_discrete_map={

                    "Benign":"#00FFB3",

                    "Attack":"#FF4D6D"
                }
            )

            pie_fig.update_layout(

                template="plotly_dark",

                height=500,

                paper_bgcolor="rgba(0,0,0,0)",

                font=dict(
                    color="white"
                )
            )

            st.plotly_chart(
                pie_fig,
                width="stretch"
            )

            # =================================
            # PREVIEW TABLE
            # =================================

            st.markdown("""

            <h2 class="section-title">

            🔍 Prediction Intelligence Preview

            </h2>

            """,
            unsafe_allow_html=True
            )

            preview_df = pd.DataFrame(

                result["results_preview"]
            )

            st.dataframe(
                preview_df,
                width="stretch"
            )

            # =================================
            # ATTACK DISTRIBUTION BAR
            # =================================

            st.markdown("""

            <h2 class="section-title">

            📊 Threat Distribution Analysis

            </h2>

            """,
            unsafe_allow_html=True
            )

            threat_fig = px.bar(

                dist_df,

                x="Traffic Type",

                y="Count",

                color="Traffic Type",

                color_discrete_map={

                    "Benign":"#00FFB3",

                    "Attack":"#FF4D6D"
                }
            )

            threat_fig.update_layout(

                template="plotly_dark",

                height=450,

                paper_bgcolor="rgba(0,0,0,0)",

                plot_bgcolor="rgba(0,0,0,0)",

                font=dict(
                    color="white"
                )
            )

            st.plotly_chart(
                threat_fig,
                width="stretch"
            )

            # =================================
            # OPERATIONAL INSIGHTS
            # =================================

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

                <h3>🌐 Why Batch Analysis Matters</h3>

                <p class="section-text">

                Enterprise cybersecurity systems
                process massive traffic volumes continuously.

                Batch inference enables:

                <ul>

                <li>Historical traffic investigation</li>

                <li>Large-scale attack hunting</li>

                <li>Threat pattern analysis</li>

                <li>Operational scalability</li>

                <li>Bulk forensic workflows</li>

                </ul>

                </p>

                </div>

                """,
                unsafe_allow_html=True
                )

            with insight2:

                st.markdown("""

                <div class="glass-card">

                <h3>⚡ Adaptive Threat Intelligence</h3>

                <p class="section-text">

                The platform combines:

                <ul>

                <li>Ensemble machine learning</li>

                <li>Probability-based scoring</li>

                <li>Explainable AI</li>

                <li>Drift monitoring</li>

                <li>Automated retraining</li>

                </ul>

                to simulate real-world
                enterprise intrusion detection workflows.

                </p>

                </div>

                """,
                unsafe_allow_html=True
                )

            # =================================
            # DOWNLOAD SECTION
            # =================================

            st.markdown("""

            <h2 class="section-title">

            ⬇️ Export Prediction Results

            </h2>

            """,
            unsafe_allow_html=True
            )

            csv = preview_df.to_csv(
                index=False
            )

            st.download_button(

                label="📥 Download Prediction Results",

                data=csv,

                file_name="enterprise_batch_predictions.csv",

                mime="text/csv"
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
— Enterprise Batch Threat Intelligence Platform

</p>

</center>

""",
unsafe_allow_html=True
)