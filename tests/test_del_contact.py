from model.contact import Contact
import random


def test_delete_contact_by_id(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="for delete"))
    old_contacts = db.get_contact_list()
    contact_to_delete = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact_to_delete.id)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
