# raise
# raise ValueError("錯誤訊息")
# except ValueError as msg:

# assert False, "錯誤訊息"
# except AssertionError as msg:

try:
    n = int(input("Please type 0 ~ 9: "))
    if n>9:
        assert False, "out of range..."
    print("You typed", n)
except AssertionError as abc:
    print(abc)
except:
    print("not a number")

