import csv
import json
import pandas as pd
def read_csv(file_path):
  # Read data from a CSV file and return as list of dicts
  with open(file_path, newline='',encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    return [row for row in reader]
def read_json(file_path):
  # Read data from JSON file and return as dict
  with open(file_path,"r",encoding="utf-8") as jsonfile:
    return json.load(jsonfile)
def read_excel(file_path, sheet_name=0):
  # Read data from an Excel file using pandas
  df = pd.read_excel(file_path, sheet_name=sheet_name)
  return df.to_dict(orient="records")