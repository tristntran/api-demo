from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

# Define the input model
class FlowerInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Define the output model
class FlowerOutput(BaseModel):
    species: str

# Endpoint to classify the flower species
@app.post("/predict", response_model=FlowerOutput)
def predict_flower_species(flower: FlowerInput):
    # Dummy logic for species classification
    species = random.choice(["setosa", "versicolor", "virginica"])
    print("predicting.")
    return FlowerOutput(species=species)
