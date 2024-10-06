from behave import given, when, then


@then('Verify there are 12 options for the settings')
def verification_12_options(context):
    context.app.verify_12_setting_options_page.verification_12_options()


@then('Verify “connect the company” button is available')
def verify_connect_comp_button(context):
    context.app.verify_12_setting_options_page.verify_connect_comp_button()



