from pathlib import Path
import csv
import json

file_path = Path("files") / "students.csv"

with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file) # this return each row as a list of values, where each value corresponds to a column in the CSV file.

    for row in reader:
        print(f"row : {row}")


#dict reader


with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file) # this return each row as a dictionary, where the keys are the column names and the values are the corresponding cell values.

    rows = list(reader)

with open("csv_json.json", "w", encoding="utf-8") as file:
    json.dump(rows, file, indent=4)  # This line serializes the rows list of dictionaries into JSON format and writes it to the "csv_json.json" file with an indentation of 4 spaces for better readability.
