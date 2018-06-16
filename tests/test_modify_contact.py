from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.fill_in_the_form(Contact(firstname="for modify"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="Olga2"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
