from behave import then


@then('Click on Secondary option at the left side menu')
def secondary_option_menu(context):
    context.app.verify_pagination_button_page.secondary_option_menu()


@then('Verify the Secondary page opens')
def verify_secondary_page(context):
    context.app.verify_pagination_button_page.verify_secondary_page()


@then('Go to the final page using the pagination button')
def final_pagination_page(context):
    context.app.verify_pagination_button_page.final_pagination_page()


@then('Go back to the first page using the pagination button')
def first_page_using_pagination_button(context):
    context.app.verify_pagination_button_page.first_page_using_pagination_button()

    