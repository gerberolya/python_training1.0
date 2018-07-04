from model.contact import Contact
import string
import random



constant_data = [
    Contact(firstname="firstname1", lastname="lastname1",
            company="company1", address="address1"),
    Contact(firstname="firstname2", lastname="lastname2",
            company="company2", address="address2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=firstname, lastname=lastname,
            company=company, address=address)
    for firstname in ["", random_string("name", 10)]
    for lastname in ["", random_string("surname", 10)]
    for company in ["", random_string("company", 10)]
    for address in ["", random_string("address", 10)]
]