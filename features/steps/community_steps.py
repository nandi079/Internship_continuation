from behave import then


@then('Click on Community option')
def click_community_option(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.community_page.click_community_option()


@then('Verify right page opens')
def right_page_verify(context):
    context.app.community_page.right_page_verify()


@then('Verify “Contact support” button is available and clickable')
def verify_contact_support_available_and_clickable(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.community_page.verify_contact_support_available_clickable()





