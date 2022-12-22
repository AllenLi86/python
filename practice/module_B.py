# if __name__ == "__main__"意義探討
# 觀察__name__隱含變數

from module_A import cool

print("__name__: ", __name__)
print("call func remotely")
cool()

# module_A.py 中的主程式在被引用的時候也被執行了，原因在於：
# 1. 當 Python 檔案（模組、module）被引用的時候，
#    檔案內的每一行都會被 Python 直譯器讀取並執行（所以 module_A.py內的程式碼會被執行）
# 2. Python 直譯器執行程式碼時，
#    有一些內建、隱含的變數，__name__就是其中之一，其意義是「模組名稱」。
#    如果該檔案是被引用，其值會是模組名稱；
#    但若該檔案是(透過命令列)直接執行，其值會是 __main__；。
