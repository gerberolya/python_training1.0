# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application




@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_contact(app):
    success = True
    app.login(username="admin", password="secret")
    app.fill_in_contacts_form(Contact(firstname="Olga", lastname="Tester", company="test_company", address="test_address", email="test123@test123.com"))
    app.logout()

