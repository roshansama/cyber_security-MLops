import pandas as pd

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from api.model_loader import (
    model
)

from api.feature_alignment import (
    align_features
)


router = APIRouter()


@router.post("/batch_predict")

async def batch_predict(
    file: UploadFile = File(...)
):

    # =================================
    # LOAD CSV
    # =================================

    df = pd.read_csv(
        file.file
    )


    # =================================
    # ALIGN FEATURES
    # =================================

    aligned_df = align_features(
        df
    )


    # =================================
    # PREDICTIONS
    # =================================

    probabilities = model.predict_proba(
        aligned_df
    )[:, 1]


    predictions = (
        probabilities >= 0.30
    ).astype(int)


    # =================================
    # SAVE RESULTS
    # =================================

    df["prediction"] = predictions

    df["attack_probability"] = (
        probabilities
    )


    # =================================
    # RETURN RESULTS
    # =================================

    return {

        "rows_processed":
            len(df),

        "attack_count":
            int(predictions.sum()),

        "benign_count":
            int(
                (predictions == 0).sum()
            ),

        "results_preview":
            df.head(10).to_dict(
                orient="records"
            )
    }