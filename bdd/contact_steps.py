from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <lastname> and <company>')
def new_contact(firstname, lastname, company):
    return Contact(firstname=firstname, lastname=lastname, company=company)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="to delete"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete random contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
   # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


@given('a new contact info with <firstname>, <lastname> and <company>')
def new_info(firstname, lastname, company):
    return Contact(firstname=firstname, lastname=lastname, company=company)

@when('I modify random contact from the list')
def modify_random_contact(app, random_contact, new_info):
    app.contact.modify_contact_by_id(random_contact.id, new_info)


@then('the new contact list is equal to the old list without deleted contact')
def verify_contact_modify(db, non_empty_contact_list, random_contact, new_info):
    old_contacts = non_empty_contact_list
    new_info.id = random_contact.id
    old_contacts.remove(random_contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(new_info)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


