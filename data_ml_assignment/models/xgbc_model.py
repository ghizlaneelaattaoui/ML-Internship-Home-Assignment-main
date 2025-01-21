import xgboost as xgb
from sklearn.pipeline import Pipeline

from data_ml_assignment.models.base_model import BaseModel


class XGBCModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(model=Pipeline([("xgbc", xgb.XGBClassifier(**kwargs))]))
