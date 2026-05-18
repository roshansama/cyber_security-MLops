import shap
import pandas as pd

from api.model_loader import model


explainer = shap.TreeExplainer(
    model
)


def generate_shap_explanation(
    input_df
):

    shap_values = explainer.shap_values(
        input_df
    )

    feature_importance = pd.DataFrame({

        "Feature": input_df.columns,

        "SHAP_Value": shap_values[0]
    })

    feature_importance = (
        feature_importance
        .sort_values(
            by="SHAP_Value",
            ascending=False
        )
    )

    return feature_importance.head(5)