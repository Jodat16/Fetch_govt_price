from fastapi import FastAPI, HTTPException
from datetime import datetime
import json

# To execute this API : uvicorn serve_prices:app --reload --host 0.0.0.0 --port 8000

app = FastAPI()


# Define route to handle date input
@app.get("/{date}")
async def get_price(date: str):
    try:

        # Load data from JSON file
        with open("price_list.json", "r") as file:
            data = json.load(file)

        # Convert input date string to datetime object
        input_date = datetime.strptime(date, "%d%b%Y").strftime("%d%b%Y")
        # Check if the date exists in the data
        if input_date in data:
            return {input_date: data[input_date]}
        else:
            raise HTTPException(status_code=404, detail="Data not found for the given date")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Please use format DDMMMYYYY (e.g., 26Mar2024)")


