from behave import then


@then('Click on User Guide option')
def user_guide_option(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    context.app.user_guide_videos_option_page.user_guide_option()


@then('Verify right page tab opens')
def verify_right_page_tab(context):
    context.app.user_guide_videos_option_page.verify_right_page_tab()


@then('Verify all lesson videos contain titles')
def verify_lesson_videos_titles(context):
    context.app.user_guide_videos_option_page.verify_lesson_videos_titles()






