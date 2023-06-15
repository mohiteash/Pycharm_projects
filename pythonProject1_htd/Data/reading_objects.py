import xlrd
path = r"C:\Users\Mohite's\Desktop\demo_exl.xlsx"

'''
def read_locators():
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name("Loginpage")
    rows = worksheet.get_rows()   # reads the data and returns a generator obj
    print(rows)
    header = next(rows)
    d = {}

    for row in rows:
        # print(row[0].value, row[1].value ,row[2].value)
        # dictionary is created to make use of it whenever required to access the value
        d[row[0].value] = (row[1].value, row[2].value)
    return d



print(read_locators())

'''

def read_locators():
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name("Loginpage")
    rows = worksheet.nrows   # reads the data and returns a generator obj
    #print(rows)
    d = {}

    for i in range(rows):
        row = worksheet.row_values(i)
        #print(row)
        d[row[0]] = (row[1], row[2])

    return d

#print(read_locators())












