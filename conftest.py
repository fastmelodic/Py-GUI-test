from comtypes.client import CreateObject
import pytest
import importlib
import os
from fixture.application import Application


@pytest.fixture(scope="session",autouse=True)
def app(request):
    fixture = Application("D:\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("xls_"):
            testdata = load_from_xls(fixture[4:])
            metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])

def load_from_xls(file):
    ap = CreateObject("Excel.Application")
    wb = ap.Workbooks.Open("%s.xlsx" % file)
    worksheet = wb.Sheets[1]
    data=[]
    for row in range(1, 11):
        data.append(worksheet.Cells[row, 1].Value())
    return data

