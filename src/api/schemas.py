from typing import Optional

from pydantic import BaseModel, Field


class HeartDataRow(BaseModel):
    id: int = Field(..., ge=0)

    age: float = Field(..., ge=0, le=1)
    blood_sugar: float = Field(..., ge=0, le=1)
    bmi: float = Field(..., ge=0, le=1)
    cholesterol: float = Field(..., ge=0, le=1)
    diastolic_blood_pressure: float = Field(..., ge=0, le=1)
    exercise_hours_per_week: float = Field(..., ge=0, le=1)
    heart_rate: float = Field(..., ge=0, le=1)
    income: float = Field(..., ge=0, le=1)
    sedentary_hours_per_day: float = Field(..., ge=0, le=1)
    systolic_blood_pressure: float = Field(..., ge=0, le=1)
    triglycerides: float = Field(..., ge=0, le=1)
    sleep_hours_per_day: float = Field(..., ge=0, le=1)

    gender: str
    diabetes: Optional[int]
    family_history: Optional[int]
    smoking: Optional[int]
    obesity: Optional[int]
    alcohol_consumption: Optional[int]
    diet: Optional[int]
    previous_heart_problems: Optional[int]
    medication_use: Optional[int]
    stress_level: Optional[int]
    physical_activity_days_per_week: Optional[int]

    class Config:
        extra = "ignore"


class PredictionOut(BaseModel):
    id: int
    prediction: int
