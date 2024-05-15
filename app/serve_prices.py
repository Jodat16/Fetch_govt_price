from fastapi import FastAPI, HTTPException
from datetime import datetime
import json

# To execute this API : uvicorn serve_prices:app --reload --host 0.0.0.0 --port 8001
app = FastAPI()

# Define route to handle date input
@app.get("/{date}")
async def get_price(date: str):
    try:

        # Load data from JSON file
        with open("price_list.json", "r") as file:
            data = json.load(file)

        # Convert input date string to datetime object
        print("Provided date in API call: ", date)
        input_date = date
        timestamp = datetime.now().strftime("%d %B %Y %H:%M:%S")
        # Check if the date exists in the data
        if input_date in data:
            print(str(timestamp) + "  --------  ")
            return {input_date: data[input_date]}
        else:
            print(str(timestamp) + "  --------  ")
            raise HTTPException(status_code=404, detail="Data not found for the given date")
    except ValueError:
        timestamp = datetime.now().strftime("%d %B %Y %H:%M:%S")
        print(str(timestamp) + "  --------  ")
        raise HTTPException(status_code=400, detail="Invalid date format. Please use format DDMMMYYYY (e.g., 26Mar2024)")


