# encoding: utf-8
import xlrd
from utils import get_file_path
from common.logger import logger

def read_excel():
    file_path = get_file_path.get_root_path()+'testdata\\testdata.xls'
    # open excel
    excel_file=xlrd.open_workbook(file_path)

    # sheet = ExcelFile.sheet_by_index(1)
    sheet = excel_file.sheet_by_name('Sheet1')

    logger.info("Read excel, sheet name {}".format(sheet.name))
    logger.info("Read excel, sheet rows {}".format(sheet.nrows))
    logger.info("Read excel, sheet cols {}".format(sheet.ncols))

    rows = sheet.row_values(1)
    cols = sheet.col_values(1)
    print(rows)
    print(cols)

    # get cell content
    print("The value of the second row and first column is: %s",sheet.cell(1,0))

    # print cell content format
    print("The cell content format is: %s",sheet.cell(0,0).ctype)

def get_xls():
    cls = []
    print("root path = ", get_file_path.get_root_path())
    file_path = get_file_path.get_root_path() + 'testdata/testdata.xls'
    print("file path", file_path)
    # file location
    excel_file = xlrd.open_workbook(file_path)
    sheet = excel_file.sheet_by_name('Sheet1')
    n_rows = sheet.nrows
    for i in range(n_rows):
        cls.append(sheet.row_values(i))
    return cls

def get_data_from_xls(path, sheet_name):
    print("get_file_path.get_root_path() = {}".format(get_file_path.get_root_path()))
    cls = []
    file_path = get_file_path.get_root_path() + path
    # file location
    excel_file = xlrd.open_workbook(file_path)
    sheet = excel_file.sheet_by_name(sheet_name)
    n_rows = sheet.nrows
    for i in range(n_rows):
        cls.append(sheet.row_values(i))
    return cls

if __name__ == '__main__':
    print(get_xls())