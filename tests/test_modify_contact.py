from model.contact import Contact


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="for modify"))
    old_contacts = app.contact.get_contact_list()
    contact_info = Contact(lastname="Tester2")
    contact_info.id = old_contacts[0].id
    app.contact.modify_first_contact(contact_info)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact_info
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
