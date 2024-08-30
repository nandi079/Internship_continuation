from behave import then


@then('Click on Change password option')
def change_password(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.user_change_password_page.change_password()


@then('Verify the right page opens as set new password')
def verify_change_password_page_opens(context):
    context.app.user_change_password_page.verify_change_password_page_opens()


@then('Add some test password to the input fields')
def add_new_password(context):
    context.app.user_change_password_page.add_new_password()


@then('Verify the “Change password” button is available')
def verify_change_password_button(context):
    context.app.user_change_password_page.verify_change_password_button()

























