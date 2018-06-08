from model.group import Group


def test_modify_name(app):
    success = True
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="modify_name"))
    app.session.logout()

def test_modify_header(app):
    success = True
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(header="modify_nheader"))
    app.session.logout()