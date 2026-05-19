import streamlit as st
import pandas as pd
import numpy as np
import random
import requests
import plotly.graph_objects as go
import plotly.express as px
import pydeck as pdk

from streamlit_autorefresh import st_autorefresh

from streamlit_agraph import (
    agraph,
    Node,
    Edge,
    Config
)

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI SOC Command Center",
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
# AUTO REFRESH
# =========================================

st_autorefresh(
    interval=4000,
    key="soc_refresh"
)

# =========================================
# SESSION STATE
# =========================================

if "packets_processed" not in st.session_state:

    st.session_state.packets_processed = 0

if "attacks_detected" not in st.session_state:

    st.session_state.attacks_detected = 0

if "drift_alerts" not in st.session_state:

    st.session_state.drift_alerts = 0

if "ai_inferences" not in st.session_state:

    st.session_state.ai_inferences = 0

# =========================================
# LOAD TEST DATA
# =========================================

df = pd.read_csv(
    "data/test/test_batch.csv"
)

sample = df.sample(1).iloc[0]

# =========================================
# API PAYLOAD
# =========================================

payload = {

    "Destination_Port":
        int(sample["Destination Port"]),

    "Flow_Duration":
        int(sample["Flow Duration"]),

    "Total_Fwd_Packets":
        int(sample["Total Fwd Packets"]),

    "Total_Backward_Packets":
        int(sample["Total Backward Packets"]),

    "Total_Length_of_Fwd_Packets":
        float(sample["Total Length of Fwd Packets"]),

    "Total_Length_of_Bwd_Packets":
        float(sample["Total Length of Bwd Packets"]),

    "Fwd_Packet_Length_Max":
        float(sample["Fwd Packet Length Max"]),

    "Bwd_Packet_Length_Max":
        float(sample["Bwd Packet Length Max"]),

    "Packet_Length_Mean":
        float(sample["Packet Length Mean"]),

    "Packet_Length_Std":
        float(sample["Packet Length Std"]),

    "Average_Packet_Size":
        float(sample["Average Packet Size"]),

    "Bwd_Packet_Length_Std":
        float(sample["Bwd Packet Length Std"]),

    "Init_Win_bytes_forward":
        float(sample["Init_Win_bytes_forward"]),

    "Init_Win_bytes_backward":
        float(sample["Init_Win_bytes_backward"])
}

# =========================================
# API CALL
# =========================================

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json=payload
)

result = response.json()

prediction = result["prediction"]

probability = (
    result["attack_probability"] * 100
)

# =========================================
# UPDATE LIVE METRICS
# =========================================

st.session_state.packets_processed += random.randint(
    1000,
    5000
)

st.session_state.ai_inferences += 1

if prediction == 1:

    st.session_state.attacks_detected += 1

if probability > 70:

    st.session_state.drift_alerts += 1

# =========================================
# HERO SECTION
# =========================================

st.markdown("""

<div class="hero-section cyber-grid">

<div class="glow-orb glow-cyan"></div>

<div class="glow-orb glow-pink"></div>

<h1 class="hero-title">

🛡️ AI Security Operations Command Center

</h1>

<p class="hero-subtitle">

Real-time adaptive cyber defense platform
powered by ensemble AI,
live threat intelligence,
drift monitoring,
and explainable intrusion detection systems.

</p>

</div>

""",
unsafe_allow_html=True
)

# =========================================
# ALERT SECTION
# =========================================

if prediction == 1:

    st.markdown("""

    <div class="glass-card live-alert">

    <h2 style="
    color:#FF4D6D;
    ">

    🚨 LIVE THREAT DETECTED

    </h2>

    <p class="section-text">

    Adaptive AI engine has identified
    anomalous network behavior.

    Threat correlation systems activated.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

else:

    st.markdown("""

    <div class="glass-card">

    <h2 style="
    color:#00FFB3;
    ">

    ✅ NETWORK STATUS STABLE

    </h2>

    <p class="section-text">

    Traffic behavior currently operating
    within acceptable threat thresholds.

    </p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# LIVE METRICS
# =========================================

metric1, metric2, metric3, metric4 = st.columns(4)

with metric1:

    st.markdown(f"""

    <div class="metric-card">

    <h3>📦 Packets Processed</h3>

    <h1>{st.session_state.packets_processed:,}</h1>

    <p>Live network flow ingestion</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric2:

    st.markdown(f"""

    <div class="metric-card">

    <h3>🚨 Attacks Detected</h3>

    <h1>{st.session_state.attacks_detected}</h1>

    <p>AI-detected threat events</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric3:

    st.markdown(f"""

    <div class="metric-card">

    <h3>🧠 AI Inferences</h3>

    <h1>{st.session_state.ai_inferences}</h1>

    <p>Real-time model decisions</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric4:

    st.markdown(f"""

    <div class="metric-card">

    <h3>🌪️ Drift Alerts</h3>

    <h1>{st.session_state.drift_alerts}</h1>

    <p>Distribution instability events</p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# SECONDARY METRICS
# =========================================

metric5, metric6, metric7, metric8 = st.columns(4)

with metric5:

    st.markdown(f"""

    <div class="metric-card">

    <h3>⚠️ Threat Probability</h3>

    <h1>{probability:.2f}%</h1>

    <p>Current attack confidence</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric6:

    st.markdown(f"""

    <div class="metric-card">

    <h3>📡 Packets/sec</h3>

    <h1>{random.randint(1000,7000)}</h1>

    <p>Real-time traffic throughput</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric7:

    st.markdown(f"""

    <div class="metric-card">

    <h3>🚨 Active Alerts</h3>

    <h1>{random.randint(1,15)}</h1>

    <p>Open SOC incidents</p>

    </div>

    """,
    unsafe_allow_html=True
    )

with metric8:

    st.markdown(f"""

    <div class="metric-card">

    <h3>🛡️ Detection Status</h3>

    <h1>{"ATTACK" if prediction == 1 else "BENIGN"}</h1>

    <p>Current AI classification</p>

    </div>

    """,
    unsafe_allow_html=True
    )

# =========================================
# LIVE TRAFFIC FEED
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

📡 Live Traffic Feed

</h2>

""",
unsafe_allow_html=True
)

traffic_data = pd.DataFrame({

    "Source IP":[

        f"192.168.1.{random.randint(1,255)}"

        for _ in range(15)
    ],

    "Destination Port":[

        random.choice([80,443,53,21,22,8080])

        for _ in range(15)
    ],

    "Protocol":[

        random.choice(["TCP","UDP"])

        for _ in range(15)
    ],

    "Threat Score":[

        round(random.uniform(0,100),2)

        for _ in range(15)
    ],

    "Status":[

        random.choice(["Benign","Attack"])

        for _ in range(15)
    ]
})

st.dataframe(
    traffic_data,
    width="stretch"
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# =========================================
# NETWORK GRAPH
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🌐 Live Network Attack Graph

</h2>

""",
unsafe_allow_html=True
)

nodes = [

    Node(
        id="Firewall",
        label="Firewall",
        size=35,
        color="#00E5FF"
    ),

    Node(
        id="IDS",
        label="AI IDS",
        size=40,
        color="#00FFB3"
    ),

    Node(
        id="Server",
        label="Core Server",
        size=35,
        color="#FF4D6D"
    )
]

for i in range(5):

    nodes.append(

        Node(

            id=f"Threat{i}",

            label=f"Threat-{i}",

            size=random.randint(15,30),

            color="#FF006E"
        )
    )

edges = [

    Edge(
        source="Firewall",
        target="IDS"
    ),

    Edge(
        source="IDS",
        target="Server"
    )
]

for i in range(5):

    edges.append(

        Edge(

            source=f"Threat{i}",

            target="Firewall",

            color="#FF006E"
        )
    )

config = Config(

    width=1200,

    height=500,

    directed=True,

    physics=True,

    hierarchical=False,

    nodeHighlightBehavior=True
)

agraph(
    nodes=nodes,
    edges=edges,
    config=config
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# =========================================
# GLOBAL THREAT MAP
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🌍 Global Threat Intelligence Map

</h2>

""",
unsafe_allow_html=True
)

attack_map_data = pd.DataFrame({

    "lat":[
        37.7749,
        55.7558,
        39.9042,
        28.6139,
        48.8566,
        -23.5505,
        35.6762
    ],

    "lon":[
        -122.4194,
        37.6173,
        116.4074,
        77.2090,
        2.3522,
        -46.6333,
        139.6503
    ],

    "country":[
        "USA",
        "Russia",
        "China",
        "India",
        "France",
        "Brazil",
        "Japan"
    ],

    "threat_level":[

        random.randint(40,100)

        for _ in range(7)
    ],

    "target_lat":[37.7749]*7,

    "target_lon":[-122.4194]*7
})

tower_layer = pdk.Layer(

    "ColumnLayer",

    data=attack_map_data,

    get_position='[lon, lat]',

    get_elevation='threat_level * 5000',

    elevation_scale=1,

    radius=80000,

    extruded=True,

    pickable=True,

    get_fill_color='[255, 0, 120, 180]'
)

arc_layer = pdk.Layer(

    "ArcLayer",

    data=attack_map_data,

    get_source_position='[lon, lat]',

    get_target_position='[target_lon, target_lat]',

    get_source_color='[255, 0, 120, 200]',

    get_target_color='[0, 255, 255, 200]',

    auto_highlight=True,

    width_scale=0.0001,

    get_width='threat_level / 8',

    pickable=True
)

view_state = pdk.ViewState(

    latitude=20,

    longitude=0,

    zoom=1.2,

    pitch=45
)

deck = pdk.Deck(

    map_style="dark",

    initial_view_state=view_state,

    layers=[

        tower_layer,
        arc_layer
    ],

    tooltip={

        "text":

        "Country: {country}\nThreat Level: {threat_level}"
    }
)

st.pydeck_chart(deck)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# =========================================
# THREAT TIMELINE
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

📈 Live Threat Timeline

</h2>

""",
unsafe_allow_html=True
)

timeline = pd.DataFrame({

    "Time": list(range(30)),

    "Threat Level":

        np.random.randint(
            0,
            100,
            30
        )
})

timeline_fig = px.line(

    timeline,

    x="Time",

    y="Threat Level",

    title="Real-Time Threat Activity"
)

timeline_fig.update_layout(

    template="plotly_dark",

    height=450,

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font=dict(
        color="white"
    )
)

st.plotly_chart(
    timeline_fig,
    width="stretch"
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# =========================================
# SHAP EXPLAINABILITY
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🧠 Real-Time AI Explainability

</h2>

""",
unsafe_allow_html=True
)

top_features = result["top_features"]

feature_names = list(
    top_features.keys()
)

feature_values = [

    abs(v)

    for v in top_features.values()
]

shap_fig = go.Figure()

shap_fig.add_trace(

    go.Bar(

        x=feature_values,

        y=feature_names,

        orientation='h'
    )
)

shap_fig.update_layout(

    template="plotly_dark",

    title="Top Responsible Features",

    height=450,

    paper_bgcolor="rgba(0,0,0,0)",

    plot_bgcolor="rgba(0,0,0,0)",

    font=dict(
        color="white"
    )
)

st.plotly_chart(
    shap_fig,
    width="stretch"
)

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# =========================================
# LIVE TERMINAL
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

🖥️ Live SIEM Terminal

</h2>

""",
unsafe_allow_html=True
)

terminal_logs = [

    "[INFO] Monitoring packet stream integrity",

    "[INFO] AI inference engine operational",

    "[WARNING] Traffic spike detected on Port 443",

    "[ALERT] Potential DDoS signature identified",

    "[INFO] Adaptive retraining policy active",

    "[INFO] Drift monitoring threshold stable",

    "[ALERT] Suspicious payload entropy detected",

    "[INFO] Threat correlation engine synchronized",

    "[WARNING] Elevated packet variance observed",

    "[INFO] Firewall routing policy updated",

    "[ALERT] Malicious traffic classification triggered",

    "[INFO] SHAP explainability pipeline completed"
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
    8
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

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# =========================================
# SOC EVENT LOGS
# =========================================

st.markdown("""

<div class="glass-card">

<h2 class="section-title">

📜 SOC Event Logs

</h2>

""",
unsafe_allow_html=True
)

logs = [

    "INFO :: Monitoring active sessions",

    "INFO :: Packet stream normalized",

    "WARNING :: Traffic spike detected",

    "ALERT :: Anomalous pattern identified",

    "INFO :: Adaptive model inference complete",

    "INFO :: Drift monitoring operational",

    "ALERT :: Threat correlation initiated",

    "INFO :: AI inference pipeline active"
]

for log in logs:

    st.code(log)

st.markdown(
    "</div>",
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
— AI Security Operations Command Center

</p>

</center>

""",
unsafe_allow_html=True
)