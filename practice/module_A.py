# 觀察__name__隱含變數

def cool():
    print("This is so cool!")
    
if __name__ == "__main__":
    print("__name__: ", __name__)
    print("call func locally")
    cool()

# Python 直譯器執行程式碼時，
# 有一些內建、隱含的變數，__name__就是其中之一，其意義是「模組名稱」。
# 如果該檔案是被引用，其值會是模組名稱；
# 但若該檔案是(透過命令列)直接執行，其值會是 __main__；。