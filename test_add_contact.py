# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def Open_home_page(self, wd):
        wd.get("http://localhost/addressbook/edit.php")

    def Login(self, wd, login, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def Open_add_new_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def Fill_in_contacts_form(self, wd, contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)

    def Save_the_contact(self, wd):
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        success = True
        wd = self.wd
        self.Open_home_page(wd)
        self.Login(wd, login="admin", password="secret")
        self.Open_add_new_contact_page(wd)
        self.Fill_in_contacts_form(wd, Contact(firstname="Olga", lastname="Tester", company="test_company", address="test_address", email="test123@test123.com"))
        self.Save_the_contact(wd)
        self.Logout(wd)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
