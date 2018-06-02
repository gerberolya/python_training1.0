# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application




@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture



def test_add_contact(app):
    success = True
    app.session.login(username="admin", password="secret")
    app.contact.fill_in_the_form(Contact(firstname="Olga", lastname="Tester", company="test_company", address="test_address", email="test123@test123.com"))
    app.session.logout()
