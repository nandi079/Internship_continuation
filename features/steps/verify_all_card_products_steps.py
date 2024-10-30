from behave import then


@then('Verify Secondary page opens')
def verification_sec_page(context):
    context.app.verify_all_card_products_page.verification_sec_page()


@then('Click on Filters')
def click_on_filters_button(context):
    context.app.verify_all_card_products_page.click_on_filters_button()


@then('Filter the products by “want to sell”')
def click_on_want_to_sell(context):
    context.app.verify_all_card_products_page.click_on_want_to_sell()


@then('Click on Apply Filter')
def click_on_apply_filter_button(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.verify_all_card_products_page.click_on_apply_filter_button()


@then('Verify all cards have “for sale” tag')
def verify_all_card_for_sale(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.verify_all_card_products_page.verify_all_card_for_sale()



