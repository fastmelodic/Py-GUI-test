import os
from comtypes.client import CreateObject


project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", 'data/')
xl = CreateObject("Excel.Application")
xl.Visible = 1
wb = xl.Workbooks.Add()
for i in range(10):
    xl.Range["A{}".format(i+1)].Value[()] = 'GROUP {}'.format(i)
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
xl.Quit()

