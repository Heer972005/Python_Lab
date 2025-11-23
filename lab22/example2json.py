import pandas as pd
json_file_path=r'G:\sem-3\python_lab\lab22\sample_data.json'
df_json=pd.read_json(json_file_path)

print("\nJSON Data:")
print(df_json)

average_age=df_json['Age'].mean()
print("\nAverage Age:", average_age)
