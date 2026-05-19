import streamlit as st
import requests
import plotly.graph_objects as go
import pandas as pd


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Threat Inference",
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
# PAGE HEADER
# =====================================

st.markdown("""

<div class="glass-card">

<h1>

🛡️ AI Threat Inference Console

</h1>

<p style="
color:#94a3b8;
font-size:18px;
line-height:1.8;
">

Real-time explainable intrusion detection powered by adaptive AI infrastructure.

</p>

</div>

""", unsafe_allow_html=True)


# =====================================
# LAYOUT
# =====================================

left_panel, right_panel = st.columns([1.1, 1])


# =====================================
# LEFT SIDE — INPUTS
# =====================================

with left_panel:

    st.markdown("""

<div class="glass-card">

<h2>

📡 Traffic Feature Input

</h2>

</div>

""", unsafe_allow_html=True)


    destination_port = st.number_input(
        "Destination Port",
        value=443
    )

    flow_duration = st.number_input(
        "Flow Duration",
        value=1200
    )

    total_fwd_packets = st.number_input(
        "Total Fwd Packets",
        value=10
    )

    total_backward_packets = st.number_input(
        "Total Backward Packets",
        value=8
    )

    total_length_fwd_packets = st.number_input(
        "Total Length of Fwd Packets",
        value=5000
    )

    total_length_bwd_packets = st.number_input(
        "Total Length of Bwd Packets",
        value=4200
    )

    fwd_packet_length_max = st.number_input(
        "Fwd Packet Length Max",
        value=1200
    )

    bwd_packet_length_max = st.number_input(
        "Bwd Packet Length Max",
        value=900
    )

    packet_length_mean = st.number_input(
        "Packet Length Mean",
        value=550
    )

    packet_length_std = st.number_input(
        "Packet Length Std",
        value=220
    )

    flow_bytes_s = st.number_input(
        "Flow Bytes/s",
        value=15000.0
    )

    flow_packets_s = st.number_input(
        "Flow Packets/s",
        value=35.0
    )

    predict_button = st.button(
        "🚀 Run Threat Detection"
    )


# =====================================
# RIGHT SIDE — RESULTS
# =====================================

with right_panel:

    st.markdown("""

<div class="glass-card">

<h2>

🧠 Threat Intelligence Output

</h2>

</div>

""", unsafe_allow_html=True)


    if predict_button:

        payload = {

    "Destination_Port":
        destination_port,

    "Flow_Duration":
        flow_duration,

    "Total_Fwd_Packets":
        total_fwd_packets,

    "Total_Backward_Packets":
        total_backward_packets,

    "Total_Length_of_Fwd_Packets":
        total_length_fwd_packets,

    "Total_Length_of_Bwd_Packets":
        total_length_bwd_packets,

    "Fwd_Packet_Length_Max":
        fwd_packet_length_max,

    "Bwd_Packet_Length_Max":
        bwd_packet_length_max,

    "Packet_Length_Mean":
        packet_length_mean,

    "Packet_Length_Std":
        packet_length_std,

    "Average_Packet_Size":
        550,

    "Bwd_Packet_Length_Std":
        220,

    "Init_Win_bytes_forward":
        65535,

    "Init_Win_bytes_backward":
        65535
}


        try:

            response = requests.post(

                "http://127.0.0.1:8000/predict",

                json=payload
            )


            result = response.json()


            prediction = result["prediction"]

            probability = result["attack_probability"]


            # ==========================
            # STATUS
            # ==========================

            if prediction == "Attack":

                st.error(
                    "🚨 MALICIOUS TRAFFIC DETECTED"
                )

                severity = "HIGH"

                severity_color = "#ff4d4d"

            else:

                st.success(
                    "✅ BENIGN TRAFFIC"
                )

                severity = "LOW"

                severity_color = "#00ff66"


            # ==========================
            # PROBABILITY GAUGE
            # ==========================

            gauge_fig = go.Figure(

                go.Indicator(

                    mode="gauge+number",

                    value=probability * 100,

                    title={
                        'text': "Threat Probability"
                    },

                    gauge={

                        'axis': {
                            'range': [0, 100]
                        },

                        'bar': {
                            'color': "#00f0ff"
                        },

                        'bgcolor': "#0f172a",

                        'borderwidth': 2,

                        'bordercolor': "#00f0ff"
                    }
                )
            )


            gauge_fig.update_layout(

                paper_bgcolor="#050b14",

                font_color="white",

                height=350
            )


            st.plotly_chart(
                gauge_fig,
                use_container_width=True
            )


            # ==========================
            # SEVERITY PANEL
            # ==========================

            st.markdown(f"""

<div class="glass-card">

<h2>

⚠️ Threat Severity

</h2>

<div style="
font-size:38px;
font-weight:800;
color:{severity_color};
margin-top:20px;
">

{severity}

</div>

</div>

""", unsafe_allow_html=True)


            # ==========================
            # SHAP VISUALIZATION
            # ==========================

            st.markdown("""

<div class="glass-card">

<h2>

🔬 Explainable AI Attribution

</h2>

</div>

""", unsafe_allow_html=True)

            top_features = result["top_features"]
            shap_features = list(
    top_features.keys()
)


            shap_values = [

    abs(v)

    for v in top_features.values()
]


            shap_fig = go.Figure(

                go.Bar(

                    x=shap_values,

                    y=shap_features,

                    orientation='h',

                    marker=dict(

                        color=shap_values,

                        colorscale='Turbo'
                    )
                )
            )


            shap_fig.update_layout(

                paper_bgcolor="#050b14",

                plot_bgcolor="#050b14",

                font_color="white",

                height=400,

                yaxis=dict(
                    autorange="reversed"
                )
            )


            st.plotly_chart(
                shap_fig,
                use_container_width=True
            )


            # ==========================
            # ANALYST GUIDANCE
            # ==========================

            st.markdown("""

<div class="glass-card">

<h2>

🛰️ SOC Analyst Recommendation

</h2>

<p style="
color:#cbd5e1;
line-height:1.9;
font-size:16px;
">

Potential anomalous traffic behavior detected.

Recommended actions:

• Inspect packet payload signatures  
• Monitor source IP reputation  
• Increase flow monitoring sensitivity  
• Verify abnormal transport behavior  
• Trigger adaptive drift monitoring  

</p>

</div>

""", unsafe_allow_html=True)


        except Exception as e:

            st.error(
                f"Inference Failed: {e}"
            )


    else:

        st.markdown("""

<div class="glass-card">

<h2>

⚡ Awaiting Threat Analysis

</h2>

<p style="
color:#94a3b8;
font-size:16px;
line-height:1.8;
">

Submit network traffic metrics to begin adaptive AI inference and explainability analysis.

</p>

</div>

""", unsafe_allow_html=True)