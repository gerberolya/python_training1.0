#from model.contact import Contact
#from random import randrange


#def test_modify_contact_lastname(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(lastname="for modify"))
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    contact_info = Contact(lastname="Tester2")
#    contact_info.id = old_contacts[index].id
#    app.contact.modify_contact_by_index(index, contact_info)
#    assert len(old_contacts) == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts[index] = contact_info
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
