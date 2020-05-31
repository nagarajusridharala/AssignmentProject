import random
import string
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from features.browser import Browser


class RegistrationPageElements(object):
    gndr1Radio = 'id_gender1'
    gndr2Radio = 'id_gender2'
    firstName = 'customer_firstname'
    lastname = 'customer_lastname'
    email = 'email'
    password = 'passwd'
    dobDay = 'days'
    dobMonth = 'months'
    dobYear = 'years'
    newsLetterChkbox = 'newsletter'
    spclOfferChkbox = 'optin'
    addrFirstName = 'firstname'
    addrLastName = 'lastname'
    company = 'company'
    address1 = 'address1'
    address2 = 'address2'
    city = 'city'
    state = 'id_state'
    country = 'id_country'
    postCode = 'postcode'
    additionalInfo = 'other'
    homePhone = 'phone'
    mobilePhone = 'phone_mobile'
    addressAlias = 'alias'
    registerButton = 'submitAccount'


class RegistrationPage(Browser):

    def select_gender(self, gendertype):
        if (gendertype == 'gender1'):
            self.driver.find_element_by_id(RegistrationPageElements.gndr1Radio).click()
        else:
            self.driver.find_element_by_id(RegistrationPageElements.gndr2Radio).click()

    def set_text_fields(self):
        first_name = RegistrationPage.random_char(8)
        last_name = RegistrationPage.random_char(8)
        password = RegistrationPage.random_char(8)
        self.driver.find_element_by_id(RegistrationPageElements.firstName).send_keys(first_name)
        self.driver.find_element_by_id(RegistrationPageElements.lastname).send_keys(last_name)
        self.driver.find_element_by_id(RegistrationPageElements.password).send_keys(password)

    def set_address_fields(self):
        self.driver.find_element_by_id(RegistrationPageElements.address1).send_keys(RegistrationPage.random_char(10))
        self.driver.find_element_by_id(RegistrationPageElements.city).send_keys(RegistrationPage.random_char(10))
        self.driver.find_element_by_id(RegistrationPageElements.postCode).send_keys("76890")
        s1 = Select(self.driver.find_element_by_id(RegistrationPageElements.country))
        s1.select_by_index(1)
        time.sleep(4)
        s2 = Select(self.driver.find_element_by_id(RegistrationPageElements.state))
        s2.select_by_visible_text("Alabama")
        self.driver.find_element_by_id(RegistrationPageElements.mobilePhone).send_keys("9808765432")
        self.driver.find_element_by_id(RegistrationPageElements.registerButton).click()

    def select_optional_fields(self):
        self.driver.find_element_by_id(RegistrationPageElements.newsLetterChkbox).click()
        self.driver.find_element_by_id(RegistrationPageElements.spclOfferChkbox).click()


    def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))
