from behave import *
from selenium import webdriver
import time


@given("launch browser")
def launch_browser(context):
    context.driver = webdriver.Chrome("C:/Users/fares/PycharmProjects/pythonProject/drivers/chromedriver.exe")


@when('login tab is open')
def open_login_tab(context):
    context.driver.get("https://gridsingularity.com/singularity-map")
    context.driver.find_element_by_xpath("/html/body/div/div[3]/div/div/div[5]/div[2]/button").click()
    time.sleep(1)
    context.driver.find_element_by_xpath("/html/body/div/div[3]/div/div/header/nav[2]/button[1]").click()
    time.sleep(2)


@when('enter email "{email}" and password "{password}"')
def enter_email_and_password(context, email, password):
    context.driver.find_element_by_xpath("/html/body/div/div[5]/div/form/div[1]/div/div/input").send_keys(email)
    context.driver.find_element_by_xpath("/html/body/div/div[5]/div/form/div[2]/div/div/input").send_keys(password)
    time.sleep(2)


@step("click on login button")
def click_login_button(context):
    context.driver.find_element_by_xpath("/html/body/div/div[5]/div/form/button").click()
    time.sleep(3)


@then("user must successfully connect to the dashboard page")
def login_successful(context):
    error = ""

    try:
        text = context.driver.find_element_by_class_name("UserAvatar_nameInitials__2m2w2").text
    except:
        try:
            error = context.driver.find_element_by_xpath("/html/body/div[1]/div[5]/div/form/div[3]").text
        except:
            context.driver.close()
            assert False, "Test Failed"

    time.sleep(2)

    if len(error) != 0:
        context.driver.close()
        assert False, error

    context.driver.close()
    assert len(str(text)) != 0, "Test Passed"
