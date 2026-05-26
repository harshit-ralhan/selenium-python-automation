import json
def load_test_data(file="data/test_data.json"):
  with open(file) as f:
    return json.load(f)