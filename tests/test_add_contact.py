# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.fill_in_the_form(Contact(firstname="Olga", lastname="Tester", company="test_company", address="test_address", email="test123@test123.com"))

