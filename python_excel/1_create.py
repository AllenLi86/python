from openpyxl import Workbook, load_workbook

# 新建檔案
wb = Workbook()
ws = wb.active
ws.title = 'new'

# 插入資料
ws.append([123,456,789,0,55])
ws.append([123,456,789,0,66])
ws.append([123,456,789,0,77])


wb.save('new_excel.xlsx')