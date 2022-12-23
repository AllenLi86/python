# pandas模組:
# 方便分析一維或二維資料的模組

import pandas as pd

phone1 = pd.Series(['apple', 'sony', 'samsung'], index=["0", "1", "2"])
print(phone1)

print(phone1[1])
print(phone1["2"])

phone2 = pd.Series(['google', 'mi'])

# ignore_index=True: index會重設
co = pd.concat([phone1, phone2], keys=["p1", "p2"], names=["series","row"])
print(co)