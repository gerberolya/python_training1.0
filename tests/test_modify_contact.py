from model.contact import Contact
import random


def test_modify_contact_lastname(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="for modify"))
    old_contacts = db.get_contact_list()
    contact_to_modify = random.choice(old_contacts)
    contact_info = Contact(lastname="Tester2")
    contact_info.id = contact_to_modify.id
    app.contact.modify_contact_by_id(contact_to_modify.id, contact_info)
    assert len(old_contacts) == app.contact.count()
    old_contacts.remove(contact_to_modify)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact_info)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
