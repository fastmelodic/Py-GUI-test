import pytest
from fixture.application import Application

@pytest.fixture(scope="session",autouse=True)
def xxx(request):
    fixture = Application("D:\\FreeAddressBookPortable\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture

