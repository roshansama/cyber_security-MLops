import streamlit as st
import requests
import pandas as pd


# =====================================
# PAGE TITLE
# =====================================

st.title(
    "🔍 Network Attack Prediction"
)

st.markdown(
    "Enter network traffic features for intrusion prediction."
)


# =====================================
# INPUT SECTION
# =====================================

col1, col2 = st.columns(2)


with col1:

    destination_port = st.number_input(
        "Destination Port",
        value=443
    )

    flow_duration = st.number_input(
        "Flow Duration",
        value=120000
    )

    total_fwd_packets = st.number_input(
        "Total Fwd Packets",
        value=35
    )

    total_backward_packets = st.number_input(
        "Total Backward Packets",
        value=28
    )

    packet_length_mean = st.number_input(
        "Packet Length Mean",
        value=145
    )


with col2:

    packet_length_std = st.number_input(
        "Packet Length Std",
        value=82
    )

    average_packet_size = st.number_input(
        "Average Packet Size",
        value=160
    )

    bwd_packet_length_std = st.number_input(
        "Bwd Packet Length Std",
        value=76
    )

    init_forward = st.number_input(
        "Init Win Bytes Forward",
        value=65535
    )

    init_backward = st.number_input(
        "Init Win Bytes Backward",
        value=65535
    )


# =====================================
# PREDICTION BUTTON
# =====================================

if st.button(
    "Predict Attack"
):

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
            4200,

        "Total_Length_of_Bwd_Packets":
            3800,

        "Fwd_Packet_Length_Max":
            950,

        "Bwd_Packet_Length_Max":
            870,

        "Packet_Length_Mean":
            packet_length_mean,

        "Packet_Length_Std":
            packet_length_std,

        "Average_Packet_Size":
            average_packet_size,

        "Bwd_Packet_Length_Std":
            bwd_packet_length_std,

        "Init_Win_bytes_forward":
            init_forward,

        "Init_Win_bytes_backward":
            init_backward
    }


    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )


    result = response.json()


    prediction = result[
        "prediction"
    ]

    probability = result[
        "attack_probability"
    ]


    # =================================
    # RESULT
    # =================================

    st.header(
        "📌 Prediction Result"
    )


    if prediction == 1:

        st.error(
            "⚠️ ATTACK DETECTED"
        )

    else:

        st.success(
            "✅ BENIGN TRAFFIC"
        )


    st.metric(
        "Attack Probability",
        round(probability, 6)
    )


    # =================================
    # SHAP FEATURES
    # =================================

    st.subheader(
        "🔬 Top Responsible Features"
    )

    shap_df = pd.DataFrame(
        result["top_features"]
    )

    st.dataframe(
        shap_df
    )