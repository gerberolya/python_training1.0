from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.fill_in_the_form(Contact(firstname="for delete"))
    app.contact.delete_first_contact()
