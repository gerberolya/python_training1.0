from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="for modify"))
    old_groups = app.group.get_group_list()
    group_info = Group(name="modify_name")
    group_info.id = old_groups[0].id
    app.group.modify_first_group(group_info)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group_info
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="for modify"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="modify_header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
