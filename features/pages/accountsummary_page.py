import random
import string

from features.browser import Browser


class AccountPageElements(object):
    SIGN_OUT = 'Sign out'


class AccountSummary(Browser):

    def verify_acount_creation_success(self):
        return self.driver.find_element_by_link_text(AccountPageElements.SIGN_OUT).is_displayed()

    def click_on_signout(self):
        self.driver.find_element_by_link_text(AccountPageElements.SIGN_OUT).click()