import allure

def after_scenario(context,scenario):
    if scenario.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        context.driver.quit()
    else:
        context.driver.quit()