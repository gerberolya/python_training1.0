from model.group import Group


def test_modify_name(app):
    app.group.modify_first_group(Group(name="modify_name"))


def test_modify_header(app):
    app.group.modify_first_group(Group(header="modify_header"))
