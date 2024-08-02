from behave import then
from time import sleep


@then('Click on Add a project')
def click_on_add_project(context):
    context.app.add_project_settings_page.click_on_add_project()


@then('Verify the right page opens')
def verify_right_page(context):
    context.app.add_project_settings_page.verify_right_page()


@then('Add some test information to the input fields')
def test_information_fields(context):
    context.app.add_project_settings_page.test_information_fields()


@then('Verify the right information is present in the input fields')
def verify_right_information(context):
    context.app.add_project_settings_page.verify_right_information()


@then('Verify “Send an application” button is available and clickable')
def verify_application_available_and_clickable(context):
    context.app.add_project_settings_page.verify_application_available_and_clickable()








