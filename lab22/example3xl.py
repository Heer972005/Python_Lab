import pandas as pd
excel_file_path=r'G:\sem-3\python_lab\lab22\sample_data.xlsx'
df_excel=pd.read_excel(excel_file_path)

print("\nExcel Data:")
print(df_excel)

entry_count=df_excel.shape[0]
print("\nNumber of entries in Excel file:",entry_count)
