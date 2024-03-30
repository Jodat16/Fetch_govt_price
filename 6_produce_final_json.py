import os
import json
from datetime import datetime

def get_max_from_json(filename):
    with open(filename, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        numbers = [int(num) for num in data["text_result"].split("\n") if num.isdigit()]
        return max(numbers)

directory = "./price_json"  # Update this with the path to your directory
output_file = "price_list.json"
today_date = datetime.today().strftime('%d%b%Y')
max_values = {}

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".json") and filename.split('_')[-1].split('.')[0] == today_date:
        filepath = os.path.join(directory, filename)
        max_value = get_max_from_json(filepath)
        max_values[filename.split('_')[0]] = max_value

# Write the max values to a new JSON file
# with open(output_file, 'w') as outfile:

#     json.dump(max_values, outfile, indent=4)

existing_file = "price_list.json"
with open(existing_file, 'r') as infile:
    existing_data = json.load(infile)
# Add max_values map against the date_today variable
existing_data[today_date] = max_values

# Write the updated content back to the JSON file
with open(existing_file, 'w') as outfile:
    json.dump(existing_data, outfile, indent=4)

print("Max values extracted and saved to", output_file)
