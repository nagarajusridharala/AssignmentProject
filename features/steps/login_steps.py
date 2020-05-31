import time

from behave import *
from nose.tools import assert_true
from features.pages.home_page import HomePage
from features.pages.signin_page import SignInPage
from features.pages.registration_page import RegistrationPage
from features.pages.accountsummary_page import AccountSummary

login_page = HomePage()
signin_page = SignInPage()
registration_page = RegistrationPage()
accountsummary_page = AccountSummary()


# navigate to gmail using the url set in home_page.py
# if title is 'Gmail' then navigation was successful
@given('user is on the login page')
def step_impl(context):
    login_page.navigate_to_signin()
    signin_page.click_on_create_account()
    time.sleep(3)


# valid username and valid password parameters are set in New_Registrations.feature
@when('user enters valid username "{username}" and valid password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


# valid username and invalid password parameters are set in New_Registrations.feature
@when('user enters valid username "{username}" and invalid password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


# if the user can access the account button and sign out then they are logged in
@then('the user is logged in')
def step_impl(context):
    context.inbox_page.logout()


# if the invalid password error appears an invalid password was entered
@then('the user is not logged in')
def step_impl(context):
    assert_true(context.login_page.get_login_error())


@step("select the gender")
def step_impl(context):
    gendertype = 'gender1'
    registration_page.select_gender(gendertype)


@step("enter firstName,lastName,password")
def step_impl(context):
    registration_page.set_text_fields()
    time.sleep(3)


@step("And enter address fields address1,address2,city,state,postalCode and country")
def step_impl(context):
    registration_page.set_address_fields()
    time.sleep(4)


@then("verify account creation is success")
def step_impl(context):
    isDiplayed = accountsummary_page.verify_acount_creation_success()
    assert_true(isDiplayed, "True")
    time.sleep(2)
    accountsummary_page.click_on_signout()


@step("select optional fields")
def step_impl(context):
    registration_page.select_optional_fields()


@step("close the browser")
def step_impl(context):
    time.sleep(4)
    registration_page.driver.quit()
