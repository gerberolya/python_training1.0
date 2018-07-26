from model.group import Group
import random
import pytest


def test_modify_group_name(app, db, check_ui):
    with pytest.allure.step('Given a non-empty group list'):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="for modify"))
        old_groups = db.get_group_list()
    group = random.choice(old_groups)
    with pytest.allure.step('When I modify random group %s from the list' % group):
        old_groups.remove(group)
        modify_group = Group(name="modify_name30")
        modify_group.id = group.id
        app.group.modify_group_by_id(group.id, modify_group)
    with pytest.allure.step('Then the new group list is equal to the old list with modifyed group'):
        assert len(old_groups) + 1 == app.group.count()
        new_groups = db.get_group_list()
        old_groups.append(modify_group)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

