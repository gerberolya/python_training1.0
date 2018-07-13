__author__ = 'tester'

from fixture.orm import ORMFixture
from model.group import Group

check = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = check.get_contacts_not_in_group(Group(id="178"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass #db.destroy()