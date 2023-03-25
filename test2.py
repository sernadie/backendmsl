import pandas as pd
import json

df = pd.read_excel("C:\Matriz.xlsx", sheet_name="Hoja1")
json_output = df.to_json(orient="records")
json_output_clean = json.dumps(json.loads(json_output), ensure_ascii=False)
print(json_output)
with open("Matriz.json", "w", encoding="utf-8") as file:
    file.write(json_output)