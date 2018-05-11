import yaml
import os
from xlrd import open_workbook


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('The yaml file is not present!')
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """
    Read excel file, and return a list.

    data in excel:
    | A  | B  | C  |
    | A1 | B1 | C1 |
    | A2 | B2 | C2 |

    If print(ExcelReader(excel, title_line=True).data), return
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    If print(ExcelReader(excel, title_line=False).data), return
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    Read the specified sheet, by index or name
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """

    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('The Excel file is not present!')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)
            if type(self.sheet) not in [int, str]:
                raise SheetTypeError(
                    'Please pass in <type int> or <type str>, not {0}'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)  # First row is title
                for col in range(1, s.nrows):
                    # Walk through the rest, pair with data in first row as dict and append to self._data
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    # Walk through all the rows and append to self._data
                    self._data.append(s.row_values(col))
        return self._data


# for testing
if __name__ == '__main__':
    y = r'E:\Test_framework\config\config.yml'
    reader = YamlReader(y)
    print(reader.data)

    e = r'E:/Test_framework/data/baidu.xlsx'
    reader = ExcelReader(e, title_line=True)
    print(reader.data)
