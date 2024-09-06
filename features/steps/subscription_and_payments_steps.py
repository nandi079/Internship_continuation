from behave import then


@then('Click on Subscription & payments option')
def click_on_subscription_and_payments(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.subscription_and_payments_page.click_on_subscription_and_payments()


@then('Verify the accurate page opens')
def verify_accurate_page_opens(context):
    context.app.subscription_and_payments_page.verify_accurate_page_opens()


@then('Verify title “Subscription & payments” is visible')
def verify_title_subscription_and_payments(context):
    context.app.subscription_and_payments_page.verify_title_subscription_and_payments()


@then('Verify “upgrade plan” and "back" buttons are available')
def verify_upgrade_plan_and_back_buttons(context):
    context.app.subscription_and_payments_page.verify_upgrade_plan_and_back_buttons()














