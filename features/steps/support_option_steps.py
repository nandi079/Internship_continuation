from behave import given, when, then


@then('Click on support option')
def click_support_button(context):
    context.app.support_option_page.click_support_button()


@then('Switch to the new tab')
def switch_new_tab_page(context):
    context.app.support_option_page.switch_new_tab_page()


@then('Verify the right support page opens')
def verify_support_page_open(context):
    context.app.support_option_page.verify_support_page_open()


@then('Go back')
def go_back_to_setting_page(context):
    context.app.support_option_page.go_back_to_setting_page()


@then('Click on news option')
def click_news_button(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.support_option_page.click_news_button()


@then('Verify the right news page opens')
def verify_news_page_open(context):
    context.app.support_option_page.verify_news_page_open()








