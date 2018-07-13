from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import encoders, decoders, convert_mysql_timestamp


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str, column="group_header")
        footer = Optional(str, column="group_footer")

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id = PrimaryKey(int, column="id")
        firstname = Optional(str, column="firstname")
        lastname = Optional(str, column="lastname")
        company = Optional(str, column="company")
        address = Optional(str, column="address")
        homephone = Optional(str, column="home")
        mobilephone = Optional(str, column="mobile")
        workphone = Optional(str, column="work")
        secondaryphone = Optional(str, column="phone2")
        email = Optional(str, column="email")
        email2 = Optional(str, column="email2")
        email3 = Optional(str, column="email3")
        deprecated = Optional(str, column="deprecated")

    def __init__(self, host, database, user, password):
        #conv = encoders
        #conv.update(decoders)
        #conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=database, user=user, password=password, conv=decoders)
        self.db.generate_mapping()

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))


    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname, company=contact.company,
                           address=contact.address, homephone=contact.home, mobilephone=contact.mobile,
                           workphone=contact.work, secondaryphone=contact.phone2,
                           email=contact.email, email2=contact.email2, email3=contact.email3)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))