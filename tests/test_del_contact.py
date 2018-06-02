

def test_add_contact(app):
    success = True
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()