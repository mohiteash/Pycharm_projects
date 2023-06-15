import xlrd
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter=True
path = r"C:\Users\Mohite's\Desktop\demo_exl.xlsx"

def read_locators():
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name("demo_web_shop")
    rows = worksheet.nrows   # reads the data and returns a generator obj
    #print(rows)
    d = {}

    for i in range(rows):
        row = worksheet.row_values(i)
        #print(row)
        d[row[0]] = (row[1], row[2])

    return d

# print(read_locators())





















