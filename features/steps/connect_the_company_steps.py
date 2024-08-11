from behave import given, when, then


@then('Click on Contact us option')
def click_contact_us(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.connect_the_company_page.click_contact_us()


@then('verify right page opening')
def verify_correct_page_opening(context):
    context.app.connect_the_company_page.verify_correct_page_opening()


@then('Verify there are at least 4 social media icons')
def verify_social_media_icons(context):
    context.app.connect_the_company_page.verify_social_media_icons()


@then('Verify “Connect the company” button is available and clickable')
def verify_connect_the_company_button_available_and_clickable(context):
    context.app.connect_the_company_page.verify_connect_the_company_button_availabe_and_clickable()

