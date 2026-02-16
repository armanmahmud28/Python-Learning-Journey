import pandas as pd

r = pd.read_json('Panda/data.json')

print(r.to_string())
