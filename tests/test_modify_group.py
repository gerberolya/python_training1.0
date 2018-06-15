from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="for modify"))
    app.group.modify_first_group(Group(name="modify_name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="for modify"))
    app.group.modify_first_group(Group(header="modify_header"))
