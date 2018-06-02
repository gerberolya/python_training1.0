from model.contact import Contact

def test_modify_first_contact(app):
    success = True
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Olga2", lastname="Tester2", company="test_company2", address="test_address2", email="test1234@test1234.com"))
    app.session.logout()