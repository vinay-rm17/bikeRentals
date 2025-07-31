from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load CSV data
df = pd.read_csv("bikes_data.csv")

@app.get("/bikes")
def get_bikes(search: str = Query(None), sort_by: str = Query("none")):
    bikes = df.copy()

    # Search by name or provider
    if search:
        bikes = bikes[bikes['Bike Name'].str.contains(search, case=False) |
                      bikes['Provider'].str.contains(search, case=False)]

    # Sorting by price
    bikes['Price (₹)'] = bikes['Price (₹)'].astype(str).str.replace("₹", "").astype(float)
    if sort_by == "low_to_high":
        bikes = bikes.sort_values(by="Price (₹)")
    elif sort_by == "high_to_low":
        bikes = bikes.sort_values(by="Price (₹)", ascending=False)

    return bikes.to_dict(orient="records")
#python -m uvicorn main:app --reload (command to run)