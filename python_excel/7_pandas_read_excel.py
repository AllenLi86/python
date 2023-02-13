import pandas as pd

# usecols = ["欄位標題"] or [欄位index] or "欄位英文代號"
df = pd.read_excel("./example.xlsx", sheet_name="ws1")
df1 = pd.read_excel("./example.xlsx", sheet_name="ws2", usecols=["data3", "data4", "data5"], nrows=6)
df2 = pd.read_excel("./example.xlsx", sheet_name="ws2", usecols=[3, 4, 5])
df3 = pd.read_excel("./example.xlsx", sheet_name="ws2", usecols="D, E:G")
df4 = pd.read_excel("./example.xlsx", sheet_name="ws2", usecols="D, E:G")

df3_row = df3[0:9]

# .at: 以 列索引值 及 欄位標題 來定位
# .iat: 以 列索引值 及 欄索引值 來定位
d1 = df.at[0, "data4"]
d2 = df.iat[0, 4]

print(df1)
print("=====")
print(df2.head(5))
print("=====")
print(df3_row)
print("=====")
print(d1)
print(d2)


