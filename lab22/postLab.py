import pandas as pd
df=pd.read_csv(r"G:\sem-3\python_lab\lab22\sample_data.csv")
#a
print(df.dtypes)

#b
df['Age']=df['Age'].fillna(df['Age'].mean())
print(df)










#Name,Age,City
#Alice,30,New York
#Bob,25,Los Angeles
#Charlie,35,Chicago