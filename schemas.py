
from pydantic import BaseModel

class PredictionResponse(BaseModel):
    prediction: int

    class Config:
        from_attributes=True