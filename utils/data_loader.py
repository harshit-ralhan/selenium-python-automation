import json
import csv
import pandas
def load_checkout_test_data(file="data/checkout_test_data.json"):
  with open(file) as f:
    return json.load(f)
def load_test_data_json(file="data/test_data.json"):
  with open(file) as f:
    data = json.load(f)
  return[v for v in data.values()]
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

def load_test_data(source="json",file_path=None):
  if source == "json":
    return load_test_data_json(file_path or "data/test_data.json")
  elif source == "csv":
    return load_test_data_csv(file_path or "data/test_data.csv")
  elif source == "excel":
    return load_test_data_excel(file_path or "data/test_data.xlsx")
  else:
    raise ValueError(f"Unsupported source: {source}")