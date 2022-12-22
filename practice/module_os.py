import os

path1 = "./abc"
path2 = "./abcde/123/456"
path3 = "./abcdefg"

# os.mkdir(path1)  # 建立單級目錄
# os.makedirs(path2)  # 建立多級目錄

# print("success")

print(os.path.exists(path3))  # 檢查路徑是否存在

print(os.path.dirname(__file__))  # 取得檔案路徑 (__file__有時候回傳相對路徑，有時候返回傳絕對路徑)
print(os.path.realpath(__file__))  # 取得檔案絕對路徑+檔名
print("")
print(os.path.dirname(os.path.realpath(__file__)))

print(os.getcwd())  # 取得當前工作路徑
