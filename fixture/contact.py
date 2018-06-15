

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_in_the_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def change_contact_form_data(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_form_data("firstname", contact.firstname)
        self.change_contact_form_data("lastname", contact.lastname)
        self.change_contact_form_data("company", contact.company)
        self.change_contact_form_data("address", contact.address)
        self.change_contact_form_data("email", contact.email)

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()



    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        # edit first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # fill form with new data
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))



