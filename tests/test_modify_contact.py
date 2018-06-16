from model.contact import Contact


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.fill_in_the_form(Contact(lastname="for modify"))
    old_contacts = app.contact.get_contact_list()
    contact_info = Contact(lastname="Tester2")
    contact_info.id = old_contacts[0].id
    app.contact.modify_first_contact(contact_info)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact_info
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
