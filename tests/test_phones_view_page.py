
def test_phones_on_contact_view_page(app):
    phones_from_view_page = app.contact.get_phones_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert phones_from_view_page.homephone == contact_from_edit_page.homephone
    assert phones_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert phones_from_view_page.workphone == contact_from_edit_page.workphone
    assert phones_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

