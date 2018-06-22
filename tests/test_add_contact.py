# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=random_string("name", 10), lastname=random_string("surname", 10),
            company=random_string("company", 10), address=random_string("address", 10))
    for firstname in ["", random_string("name", 10)]
    for lastname in ["", random_string("surname", 10)]
    for company in ["", random_string("company", 10)]
    for address in ["", random_string("address", 10)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

