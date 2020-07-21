from src.common import log
from config.globalparameter import test_data_path
import xlrd

# an easy life is rarely meaningful and a meaningful life rarely easy

class Excel(object):
    def __init__(self):
        self.excel_log = log.log()

    def open_excel(self, file):
        """读取excel文件"""
        try:
            data = xlrd.open_workbook(file)
            return data
        except Exception as e:
            self.excel_log.error(u"打开excel文件失败")

    # def data_excel(self, file, sheetName):
    #     """封装list"""
    #     data = self.open_excel(file)
    #     # 通过工作表名称，获取到一个工作表
    #     table = data.sheet_by_name(sheetName)
    #     # 获取行数
    #     trows = table.nrows
    #     # 获取 第一行数据
    #     tcolnames = table.row_values(0)
    #     restul_list = []
    #     for rownumber in range(1, trows):
    #         row = table.row_values(rownumber)
    #         if row:
    #             app = {}
    #             for i in range(len(tcolnames)):
    #                 app[tcolnames[i]] = row[i]
    #                 restul_list.append(app)
    #     return restul_list

    def read_excel(self, file, colnameindex=0, by_index=0):
        data = self.open_excel(file)
        table = data.sheet_by_index(by_index)
        nrow = table.nrows
        ncol = table.ncols
        colname = table.row_values(colnameindex)
        test_data = []
        for r in range(colnameindex + 1, nrow):
            row = table.row_values(r)
            res = {}
            if row:
                for c in range(ncol):
                    if colname[c] != "":
                        if isinstance(row[c], float):
                            res[colname[c]] = str(int(row[c]))
                        else:
                            res[colname[c]] = row[c]
            test_data.append(res)
        return test_data

    def get_list(self, by_index):
        try:
            data_list = self.read_excel(test_data_path,colnameindex=0, by_index=0)
            assert len(data_list) >= 0, u'excel标签页:'+by_index+u'为空'
            return data_list
        except Exception as e:
            self.excel_log.error(u'excel标签页:'+by_index+u'为空')
            raise e

if __name__ == '__main__':
    ex = Excel()
    ex.read_excel(test_data_path, 0, 0)
    print(ex.read_excel(test_data_path, 0, 0))