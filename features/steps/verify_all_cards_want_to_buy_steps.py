from behave import then


@then('the products by “want to buy”')
def click_on_want_to_buy(context):
    context.app.verify_all_cards_want_to_buy_page.click_on_want_to_buy()


@then('Verify all cards have “Want to buy” tag')
def verify_all_card_want_to_buy(context):
    context.app.verify_all_cards_want_to_buy_page.verify_all_card_want_to_buy()





