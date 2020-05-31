from features.browser import Browser
from selenium import webdriver


class HomePageElements(object):
    SIGN_IN = 'Sign in'


class HomePage(Browser):
    # login page actions

    def navigate_to_signin(self):
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.find_element_by_link_text(HomePageElements.SIGN_IN).click()
