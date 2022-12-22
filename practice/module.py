import random
import string

num = string.digits
eng = string.ascii_letters
all = list(num + eng)

random.shuffle(all)
length= int(input("密碼長度: "))

pwd = "".join(all[:length])

print(pwd)