import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO


# =====================================
# PAGE TITLE
# =====================================

st.title(
    "📂 Batch CSV Prediction"
)

st.markdown(
    "Upload network traffic CSV files for large-scale intrusion analysis."
)


# =====================================
# FILE UPLOAD
# =====================================

uploaded_file = st.file_uploader(

    "Upload CSV File",

    type=["csv"]
)


# =====================================
# PROCESS FILE
# =====================================

if uploaded_file is not None:

    st.success(
        "CSV Uploaded Successfully"
    )


    # =================================
    # SEND TO FASTAPI
    # =================================

    files = {

        "file": (

            uploaded_file.name,

            uploaded_file,

            "text/csv"
        )
    }


    if st.button(
        "Run Batch Prediction"
    ):

        with st.spinner(
            "Running Batch Inference..."
        ):

            response = requests.post(

                "http://127.0.0.1:8000/batch_predict",

                files=files
            )


        result = response.json()


        # =================================
        # SUMMARY METRICS
        # =================================

        st.header(
            "📊 Batch Summary"
        )

        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Rows Processed",
                result["rows_processed"]
            )


        with col2:

            st.metric(
                "Detected Attacks",
                result["attack_count"]
            )


        with col3:

            st.metric(
                "Benign Traffic",
                result["benign_count"]
            )


        # =================================
        # RESULTS PREVIEW
        # =================================

        st.header(
            "🔍 Prediction Preview"
        )

        preview_df = pd.DataFrame(

            result["results_preview"]
        )

        st.dataframe(
            preview_df
        )


        # =================================
        # PIE CHART
        # =================================

        st.header(
            "📈 Traffic Distribution"
        )

        labels = [

            "Benign",

            "Attack"
        ]

        values = [

            result["benign_count"],

            result["attack_count"]
        ]


        fig, ax = plt.subplots(
            figsize=(6, 6)
        )

        ax.pie(

            values,

            labels=labels,

            autopct="%1.1f%%"
        )

        ax.set_title(
            "Traffic Classification"
        )

        st.pyplot(fig)


        # =================================
        # DOWNLOADABLE CSV
        # =================================

        st.header(
            "⬇️ Download Results"
        )

        csv = preview_df.to_csv(
            index=False
        )


        st.download_button(

            label="Download Prediction Preview",

            data=csv,

            file_name="prediction_results.csv",

            mime="text/csv"
        )