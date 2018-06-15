from model.contact import Contact


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.fill_in_the_form(Contact(firstname="for modify"))
    app.contact.modify_first_contact(Contact(firstname="Olga2"))
