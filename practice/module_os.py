import os

path1 = "./abc"
path2 = "./abcde/123/456"
path3 = "./abcdefg"

# os.mkdir(path1)  # 建立單級目錄
# os.makedirs(path2)  # 建立多級目錄

# print("success")

print(1, os.path.exists(path3))  # 檢查路徑是否存在

print(2, os.path.dirname(__file__))  # 取得檔案路徑 (__file__有時候回傳相對路徑，有時候回傳絕對路徑)
print(3, os.path.dirname("D:\\vsc\\python\\practice\\class.py"))
print(4, os.path.basename(__file__))  # 取得檔名
print(5, os.path.realpath(__file__))  # 取得檔案絕對路徑+檔名
print(6, os.path.dirname(os.path.realpath(__file__)))

print(7, os.path.split(os.path.realpath(__file__)))  # tuple型態回傳檔案的絕對路徑和檔案名稱，路徑和名稱分開

print(8, os.getcwd())  # 取得當前工作路徑
