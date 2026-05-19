import streamlit as st
import pandas as pd
import plotly.express as px

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Data Dictionary",
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

📚 Network Traffic Intelligence Portal

</h1>

<p class="hero-subtitle">

Deep technical documentation covering
dataset structure,
attack behavior,
network flow intelligence,
feature engineering,
and cybersecurity domain understanding.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# DATASET OVERVIEW
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🗂️ Dataset Overview

</h2>

<p class="section-text">

This project uses the
<b>CICIDS2017 Dataset</b>
created by the
Canadian Institute for Cybersecurity.

The dataset was designed to simulate
realistic enterprise network traffic
containing both:

<ul>

<li>Benign user behavior</li>

<li>Modern cyber attacks</li>

</ul>

Unlike older IDS datasets,
CICIDS2017 includes:

<ul>

<li>Realistic network flow patterns</li>

<li>Modern attack strategies</li>

<li>Application-level attacks</li>

<li>Volumetric attacks</li>

<li>Brute-force authentication attacks</li>

<li>Web exploitation attempts</li>

</ul>

The dataset is widely used in:
<ul>

<li>Intrusion Detection Research</li>

<li>Cybersecurity ML Systems</li>

<li>Anomaly Detection Research</li>

<li>Network Traffic Intelligence</li>

</ul>

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# ATTACK CLASS ENCYCLOPEDIA
# =========================================

st.markdown("""

<h2 class="section-title">

🚨 Attack Class Encyclopedia

</h2>

""",
unsafe_allow_html=True
)

attack_classes = [

    {
        "Attack":"DDoS",
        "Description":"Distributed traffic flooding attack designed to overwhelm infrastructure resources.",
        "Impact":"Service outages, bandwidth exhaustion, server crashes."
    },

    {
        "Attack":"PortScan",
        "Description":"Reconnaissance technique used to identify open services and vulnerable ports.",
        "Impact":"Pre-attack intelligence gathering."
    },

    {
        "Attack":"Botnet",
        "Description":"Compromised devices remotely controlled to launch coordinated attacks.",
        "Impact":"Large-scale distributed attacks and malware propagation."
    },

    {
        "Attack":"Brute Force",
        "Description":"Repeated authentication attempts to crack credentials.",
        "Impact":"Unauthorized system access."
    },

    {
        "Attack":"DoS Hulk",
        "Description":"High-volume HTTP flooding attack targeting web services.",
        "Impact":"Application unavailability."
    },

    {
        "Attack":"Slowloris",
        "Description":"Slow HTTP attack keeping connections partially open.",
        "Impact":"Connection pool exhaustion."
    },

    {
        "Attack":"Web Attack",
        "Description":"Injection or application-layer exploitation attempt.",
        "Impact":"Data theft, privilege escalation."
    },

    {
        "Attack":"FTP Patator",
        "Description":"Automated FTP credential attack.",
        "Impact":"FTP account compromise."
    },

    {
        "Attack":"SSH Patator",
        "Description":"Automated SSH password guessing attack.",
        "Impact":"Remote infrastructure compromise."
    }
]

attack_df = pd.DataFrame(
    attack_classes
)

st.dataframe(
    attack_df,
    width="stretch"
)

# =========================================
# WHY ATTACKS LOOK DIFFERENT
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🧠 Why Machine Learning Can Detect These Attacks

</h2>

<p class="section-text">

Cyber attacks alter normal traffic behavior.

Examples:

<ul>

<li>DDoS attacks create abnormal packet rates and traffic spikes</li>

<li>Port scanning generates repeated small connection attempts</li>

<li>Brute-force attacks produce repeated authentication patterns</li>

<li>Botnet activity creates synchronized anomalous flows</li>

<li>Slowloris attacks manipulate connection timing behavior</li>

</ul>

Machine learning models identify these behavioral anomalies
using statistical traffic features such as:

<ul>

<li>Packet size distributions</li>

<li>Traffic rates</li>

<li>Connection duration</li>

<li>Inter-arrival times</li>

<li>TCP window behavior</li>

<li>Flow statistics</li>

</ul>

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# NETWORK FLOW CONCEPTS
# =========================================

st.markdown("""

<h2 class="section-title">

🌐 Network Flow Intelligence Concepts

</h2>

""",
unsafe_allow_html=True
)

concept1, concept2 = st.columns(2)

with concept1:

    st.markdown("""

    <div class="glass-card">

    <h3>What Is A Network Flow?</h3>

    <p class="section-text">

    A network flow represents a sequence of packets
    exchanged between two endpoints during communication.

    A flow may contain:

    <ul>

    <li>Packet counts</li>

    <li>Byte transfers</li>

    <li>Timing information</li>

    <li>TCP session statistics</li>

    </ul>

    Intrusion detection systems analyze flow behavior
    instead of inspecting every raw packet individually.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

with concept2:

    st.markdown("""

    <div class="glass-card">

    <h3>Why Statistical Features Matter</h3>

    <p class="section-text">

    Attacks rarely look identical at packet level.

    Instead,
    malicious behavior often changes:

    <ul>

    <li>Packet timing</li>

    <li>Traffic burst rates</li>

    <li>Connection duration</li>

    <li>Packet variability</li>

    <li>Directional imbalance</li>

    </ul>

    Statistical ML features help models
    identify these hidden behavioral signatures.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# FULL FEATURE DICTIONARY
# =========================================

st.markdown("""

<h2 class="section-title">

📖 Full Feature Dictionary

</h2>

""",
unsafe_allow_html=True
)

feature_data = {

    "Feature":[

        "Destination Port",
        "Flow Duration",
        "Total Fwd Packets",
        "Total Backward Packets",
        "Total Length of Fwd Packets",
        "Total Length of Bwd Packets",
        "Fwd Packet Length Max",
        "Fwd Packet Length Min",
        "Fwd Packet Length Mean",
        "Fwd Packet Length Std",
        "Bwd Packet Length Max",
        "Bwd Packet Length Min",
        "Bwd Packet Length Mean",
        "Bwd Packet Length Std",
        "Flow Bytes/s",
        "Flow Packets/s",
        "Flow IAT Mean",
        "Flow IAT Std",
        "Flow IAT Max",
        "Flow IAT Min",
        "Fwd IAT Total",
        "Fwd IAT Mean",
        "Fwd IAT Std",
        "Fwd IAT Max",
        "Fwd IAT Min",
        "Bwd IAT Total",
        "Bwd IAT Mean",
        "Bwd IAT Std",
        "Bwd IAT Max",
        "Bwd IAT Min",
        "Fwd PSH Flags",
        "Bwd PSH Flags",
        "Fwd URG Flags",
        "Bwd URG Flags",
        "Fwd Header Length",
        "Bwd Header Length",
        "Fwd Packets/s",
        "Bwd Packets/s",
        "Min Packet Length",
        "Max Packet Length",
        "Packet Length Mean",
        "Packet Length Std",
        "Packet Length Variance",
        "FIN Flag Count",
        "SYN Flag Count",
        "RST Flag Count",
        "PSH Flag Count",
        "ACK Flag Count",
        "URG Flag Count",
        "CWE Flag Count",
        "ECE Flag Count",
        "Down/Up Ratio",
        "Average Packet Size",
        "Avg Fwd Segment Size",
        "Avg Bwd Segment Size",
        "Fwd Header Length.1",
        "Subflow Fwd Packets",
        "Subflow Fwd Bytes",
        "Subflow Bwd Packets",
        "Subflow Bwd Bytes",
        "Init_Win_bytes_forward",
        "Init_Win_bytes_backward",
        "act_data_pkt_fwd",
        "min_seg_size_forward",
        "Active Mean",
        "Active Std",
        "Active Max",
        "Active Min"
    ]
}

feature_df = pd.DataFrame(feature_data)

feature_df["Category"] = feature_df["Feature"].apply(

    lambda x:

    "Packet Statistics"

    if "Packet" in x

    else

    "Flow Statistics"

    if "Flow" in x

    else

    "TCP/Protocol Features"

    if "Flag" in x or "Win" in x

    else

    "Traffic Direction Features"
)

feature_df["Why It Matters"] = feature_df["Category"].map({

    "Packet Statistics":
        "Packet behavior changes significantly during attacks.",

    "Flow Statistics":
        "Flow timing and rate anomalies often reveal malicious behavior.",

    "TCP/Protocol Features":
        "TCP session anomalies help detect exploitation attempts.",

    "Traffic Direction Features":
        "Directional imbalance often reveals scans or flooding attacks."
})

st.dataframe(
    feature_df,
    width="stretch"
)

# =========================================
# DATA QUALITY CHALLENGES
# =========================================

st.markdown("""

<h2 class="section-title">

⚠️ Data Quality Challenges

</h2>

""",
unsafe_allow_html=True
)

st.markdown("""

<div class="glass-card">

<h3>Key Challenges Encountered</h3>

<ul>

<li><b>Class Imbalance</b> — benign traffic heavily dominated attack traffic</li>

<li><b>Infinite Values</b> — generated during rate-based calculations</li>

<li><b>Missing Values</b> — required cleaning and validation</li>

<li><b>Feature Distribution Drift</b> — traffic behavior changes over time</li>

<li><b>High Feature Correlation</b> — several packet statistics were strongly related</li>

<li><b>Object-Type Columns</b> — categorical columns required preprocessing</li>

</ul>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# PREPROCESSING PIPELINE
# =========================================

st.markdown("""

<h2 class="section-title">

🛠️ Data Cleaning & Preprocessing Pipeline

</h2>

""",
unsafe_allow_html=True
)

pipeline_steps = [

    "Raw CSV Loading",

    "Merge Traffic Files",

    "Handle Missing Values",

    "Replace Infinite Values",

    "Drop Invalid Rows",

    "Drop Object Columns",

    "Feature Alignment",

    "Train/Test Split",

    "Model Training"
]

pipeline_df = pd.DataFrame({

    "Step": pipeline_steps,

    "Stage":

        list(range(
            1,
            len(pipeline_steps)+1
        ))
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

    showlegend=False,

    yaxis_visible=False,

    height=350
)

st.plotly_chart(
    fig,
    width="stretch"
)

# =========================================
# SECURITY ENGINEERING INSIGHTS
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🔍 Security Engineering Insights

</h2>

<p class="section-text">

Intrusion detection is fundamentally a behavioral analysis problem.

Traditional rule-based systems fail because:
<ul>

<li>Attack signatures constantly evolve</li>

<li>Zero-day attacks bypass static rules</li>

<li>Large-scale traffic is difficult to inspect manually</li>

</ul>

Machine learning improves detection by:
<ul>

<li>Learning hidden traffic patterns</li>

<li>Detecting statistical anomalies</li>

<li>Generalizing across unseen attacks</li>

<li>Identifying behavioral deviations</li>

</ul>

However,
production IDS systems must also handle:
<ul>

<li>Data drift</li>

<li>Changing traffic distributions</li>

<li>False positives</li>

<li>Class imbalance</li>

<li>Inference scalability</li>

<li>Explainability requirements</li>

</ul>

This project was designed to address all of these operational challenges.

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
— Security Intelligence Documentation

</p>

</center>

""",
unsafe_allow_html=True
)