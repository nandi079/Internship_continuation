from behave import then


@then('Filter the products by price range from 1200000 to 2000000 AED')
def add_price_range_from_unit(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.verify_unit_price_range_page.add_price_range_from_unit()


@then('Verify the price in all cards is inside the range (1200000 - 2000000)')
def verify_all_cards_inside_range(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.verify_unit_price_range_page.verify_all_cards_inside_range()


















