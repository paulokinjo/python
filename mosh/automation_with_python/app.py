import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet1']

for row in range(2, sheet.max_row + 1):
    col_cell = 'c' + str(row)
    row_cell = sheet[col_cell]
    print(row_cell.value)