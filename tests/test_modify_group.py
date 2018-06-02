from model.group import Group


def test_modify_first_group(app):
    success = True
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="modify_name", header="modify_header", footer="modify_footer"))
    app.session.logout()