stock = [
    {
        "brand": "apple",
        "model": "iphone 14 pro max",
        "color": "purple",
        "capacity": 256
    },
    {
        "brand": "samsung",
        "model": "galaxy s22 ultra",
        "color": "black",
        "capacity": 512
    },
    {
        "brand": "google",
        "model": "pixel 5a",
        "color": "green",
        "capacity": 128
    },
]

q = "0"

while q != "":
    q = input("請輸入欲查詢的手機(或是按Enter退出): ").lower()
    
    if q in str(stock):
        for i in stock:            
            if i["brand"] == q:
                print(f"{q}庫存型號是{i['model']}，{i['color']}，{i['capacity']}G")
            elif q in i["model"]:
                print(f"{q}庫存還有{i['brand']} {i['model']}，{i['color']}，{i['capacity']}G")
            elif q in i["color"]:
                print(f"{q}庫存還有{i['brand']} {i['model']}，{i['capacity']}G")
    else:
        print(f"目前沒有{q}的庫存")