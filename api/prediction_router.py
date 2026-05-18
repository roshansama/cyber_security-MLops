import pandas as pd

from fastapi import APIRouter

from api.schemas import (
    NetworkTrafficInput
)

from api.model_loader import (
    model
)

from api.shap_explainer import (
    generate_shap_explanation
)

from api.feature_alignment import (
    align_features
)


router = APIRouter()


@router.post("/predict")

def predict_attack(
    data: NetworkTrafficInput
):

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


    # ================================
    # ALIGN FEATURES
    # ================================

    aligned_input = align_features(
        input_data
    )


    # ================================
    # PREDICTION
    # ================================

    probability = model.predict_proba(
        aligned_input
    )[0][1]

    prediction = int(
        probability >= 0.30
    )


    # ================================
    # SHAP EXPLANATION
    # ================================

    shap_results = (
        generate_shap_explanation(
            aligned_input
        )
    )


    return {

        "prediction": prediction,

        "attack_probability":
            float(probability),

        "top_features":
            shap_results.to_dict(
                orient="records"
            )
    }