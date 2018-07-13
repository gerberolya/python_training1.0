from model.contact import Contact
import re


def test_contacts_on_main_page_and_db_the_same(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Olga", lastname="Tester", address="for_test",
                       homephone="123321", mobilephone="456654",
                       workphone="789987", secondaryphone="098890",
                       email="test@test.com", email2="test@test.com2", email3="test@test.com3"))
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(contacts_from_home_page) == len(contacts_from_db)
    for num in range(len(contacts_from_db)):
        assert contacts_from_home_page[num].lastname == contacts_from_db[num].lastname
        assert contacts_from_home_page[num].firstname == clear(contacts_from_db[num].firstname)
        assert contacts_from_home_page[num].address == clear(contacts_from_db[num].address)
        assert contacts_from_home_page[num].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[num])
        assert contacts_from_home_page[num].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[num])


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email2, contact.email3]))


def clear(s):
    return re.sub('[() -]', '', s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))