from behave import then
from time import sleep


@then('Click on Main-menu at the left side menu')
def click_on_main_menu(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.task4_page.click_on_main_menu()


@then('Change the language of the page to Russian')
def click_on_language_page(context):
    context.app.task4_page.click_on_language_page()


@then('Verify the language has changed')
def verify_the_language(context):
    context.app.task4_page.verify_the_language()






