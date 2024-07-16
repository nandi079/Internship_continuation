from behave import given, when, then
from time import sleep


@given('Open the Relly main page')
def open_page(context):
    context.app.main_page.open_main()
    context.app.signin_page.verify_signin_page()
    sleep(3)


@then('Input email {expected_field} is entered')
def input_field(context,expected_field):
    context.app.signin_page.input_field(expected_field)


@then('Input password field {expected_field} is entered')
def password_field(context,expected_field):
    context.app.signin_page.password_field(expected_field)


@then('Click on Continue button')
def submit_login(context):
    context.app.signin_page.click_submit_login()


@then('Verify {user} logged in')
def verify_login(context,user):
    context.app.signin_page.verify_user_loggedin(user)


@then('Click on Off-plan at the left side menu')
def click_on_text(context):
    context.app.main_page.click_on_text()


@then('Open filter window')
def open_filter_window(context):
    context.app.main_page.open_filter_window()


@then('Filter by sale status of “Newly Launched”')
def open_newlaunch_filter(context):
    context.app.main_page.open_newlaunch_filter()


@then('Verify each product contains the Newly Launched tag')
def verify_newlaunch_tag(context):
    context.app.main_page.verify_newlaunch_tag()


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()


@when('Log in to the page')
def login(context):
    context.app.main_page.login()


@then('Click on the Continue button')
def click_on_continue(context):
    context.app.main_page.click_on_continue()


@when('Click on Connect the company')
def click_on_company(context):
    context.app.main_page.click_on_company()


@then('Switch the new tab')
def switch_new_tab(context):
    context.app.main_page.switch_new_tab()


@then('Verify the right tab opens')
def switch_new_tab(context):
    context.app.main_page.switch_new_tab()


@then('Click on settings option')
def click_on_settings(context):
    context.driver.execute_script("window.scrollBy(0,2000)","")
    context.app.main_page.click_on_settings()


@then('Click on Edit profile option')
def click_on_edit(context):
    context.app.main_page.click_on_edit()


@then('Enter expected text in the expected fields')
def test_information_input_fields(context):
    sleep(5)
    context.app.main_page.test_information_input_fields()


@then('Check the right information is present in the input fields.')
def verify_information_input_fields(context):
    context.app.main_page.verify_information_input_fields()


@then('Check “Close” and “Save Changes” buttons are available and clickable.')
def verify_close_save_buttons(context):
    context.app.main_page.verify_close_save_buttons()









