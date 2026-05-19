import pandas as pd
import shap

from fastapi import APIRouter

from api.schemas import (
    NetworkTrafficInput
)

from api.model_loader import (
    model
)

from api.feature_alignment import (
    align_features
)


# =====================================
# ROUTER
# =====================================

router = APIRouter()


# =====================================
# SHAP EXPLAINER
# =====================================

explainer = shap.TreeExplainer(
    model
)


# =====================================
# PREDICTION ENDPOINT
# =====================================

@router.post("/predict")

def predict_attack(
    data: NetworkTrafficInput
):

    # =================================
    # INPUT DATAFRAME
    # =================================

    input_data = pd.DataFrame([{

        "Destination Port":
            data.Destination_Port,

        "Flow Duration":
            data.Flow_Duration,

        "Total Fwd Packets":
            data.Total_Fwd_Packets,

        "Total Backward Packets":
            data.Total_Backward_Packets,

        "Total Length of Fwd Packets":
            data.Total_Length_of_Fwd_Packets,

        "Total Length of Bwd Packets":
            data.Total_Length_of_Bwd_Packets,

        "Fwd Packet Length Max":
            data.Fwd_Packet_Length_Max,

        "Bwd Packet Length Max":
            data.Bwd_Packet_Length_Max,

        "Packet Length Mean":
            data.Packet_Length_Mean,

        "Packet Length Std":
            data.Packet_Length_Std,

        "Average Packet Size":
            data.Average_Packet_Size,

        "Bwd Packet Length Std":
            data.Bwd_Packet_Length_Std,

        "Init_Win_bytes_forward":
            data.Init_Win_bytes_forward,

        "Init_Win_bytes_backward":
            data.Init_Win_bytes_backward
    }])


    # =================================
    # FEATURE ALIGNMENT
    # =================================

    aligned_input = align_features(
        input_data
    )


    # =================================
    # MODEL PREDICTION
    # =================================

    probability = model.predict_proba(
        aligned_input
    )[0][1]


    prediction = int(
        probability >= 0.30
    )


    prediction_label = (

        "Attack"

        if prediction == 1

        else "Benign"
    )


    # =================================
    # SHAP VALUES
    # =================================

    shap_values = explainer.shap_values(
        aligned_input
    )


    # =================================
    # HANDLE XGBOOST OUTPUT
    # =================================

    if isinstance(
        shap_values,
        list
    ):

        shap_array = shap_values[1][0]

    else:

        shap_array = shap_values[0]


    # =================================
    # FEATURE IMPORTANCE
    # =================================

    feature_importance = dict(

        zip(

            aligned_input.columns,

            shap_array.tolist()
        )
    )


    # =================================
    # TOP FEATURES
    # =================================

    top_features = dict(

        sorted(

            feature_importance.items(),

            key=lambda x: abs(x[1]),

            reverse=True

        )[:5]
    )


    # =================================
    # RESPONSE
    # =================================

    return {

        "prediction":
            prediction_label,

        "attack_probability":
            float(probability),

        "top_features":
            top_features
    }