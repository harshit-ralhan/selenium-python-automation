import json
import csv
import pandas
def load_test_data_json(file="data/test_data.json"):
  with open(file) as f:
    return json.load(f)
def load_test_data_csv(file_path="data/test_data.csv"):
  data = []
  with open(file_path,newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
      data.append(row)
  return data
def load_test_data_excel(file_path="data/test_data.xlsx"):
  data_frame = pandas.read_excel(file_path)
  return data_frame.to_dict(orient="records")