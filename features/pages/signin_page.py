import random
import string

from features.browser import Browser


class SignInPageElements(object):
    emailInput = 'email_create'
    createAccountButton = 'SubmitCreate'


class SignInPage(Browser):
    # inbox actions

    def click_on_create_account(self):
        self.driver.find_element_by_id(SignInPageElements.emailInput).send_keys(SignInPage.random_char(7))
        self.driver.find_element_by_id(SignInPageElements.createAccountButton).click()

    def random_char(y):
        rando_string = ''.join(random.choice(string.ascii_letters) for x in range(y))
        return rando_string + "@gmail.com"

    # def navigate_to_inbox(self):
    #     self.driver.get(InboxPageElements.INBOX_PAGE)
    #
    # def assert_login_success(self):
    #     # if account button is present we have logged in
    #     assert_true(self.driver.find_element_by_css_selector(InboxPageElements.ACCOUNT_BUTTON))
    #
    # def get_page_title(self):
    #     return self.driver.title
    #
    # def message_sent_assert(self):
    #     view_message_link = WebDriverWait(self.driver, 1000).until(
    #         EC.presence_of_element_located((By.XPATH, InboxPageElements.RESULT))
    #     )
    #     view_message_link.click()
    #
    # def select_message(self):
    #     select_button = WebDriverWait(self.driver, 1000).until(
    #         EC.presence_of_element_located((By.XPATH, InboxPageElements.MESSAGE_SELECT))
    #     )
    #     select_button.click()
    #
    # def compose_message(self, recipient, subject, message):
    #     compose_button = WebDriverWait(self.driver, 1000).until(
    #         EC.presence_of_element_located((By.XPATH, InboxPageElements.COMPOSE))
    #     )
    #     compose_button.click()
    #
    #     self.driver.find_element_by_xpath(InboxPageElements.RECIPIENT).send_keys(recipient)
    #     self.driver.find_element_by_xpath(InboxPageElements.SUBJECT).send_keys(subject)
    #     self.driver.find_element_by_xpath(InboxPageElements.MESSAGE).send_keys(message)
    #
    # def send_message(self):
    #     self.driver.find_element_by_xpath(InboxPageElements.SEND).click()
    #
    # def search_for_message(self, search_term):
    #     search = WebDriverWait(self.driver, 1000).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, InboxPageElements.SEARCH))
    #     )
    #     search.send_keys(search_term)
    #     search.send_keys(Keys.ENTER)
    #
    # def filter_result(self):
    #     self.select_message()
    #
    # def delete_message(self):
    #     WebDriverWait(self.driver, 1000)
    #     self.select_message()
    #     self.driver.find_element_by_xpath(InboxPageElements.DELETE).click()
    #
    # def delete_success(self):
    #     self.driver.find_element_by_css_selector(InboxPageElements.DELETE_SUCCESS)
    #
    # def move_message_to_folder(self, folder_name):
    #     WebDriverWait(self.driver, 1000)
    #
    #     self.select_message()
    #
    #     wait_for_folder_dropdown = WebDriverWait(self.driver, 1000).until(
    #         EC.presence_of_element_located((By.XPATH, InboxPageElements.MOVE_TO))
    #     )
    #     wait_for_folder_dropdown.click()
    #
    #     actions = ActionChains(self.driver)
    #     actions.send_keys(folder_name)
    #     actions.perform()
    #
    #     self.driver.find_element_by_xpath('//span[contains(text(), "Test Folder"]').click()
    #
    # def assert_message_moved(self, folder_name):
    #     self.driver.find_element_by_xpath('//span[@title="' + folder_name + '"]').click()
    #     self.delete_message()
    #
    # def logout(self):
    #     account_button = WebDriverWait(self.driver, 1000).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, InboxPageElements.ACCOUNT_BUTTON))
    #     )
    #     account_button.click()
    #
    #     self.driver.find_element_by_css_selector(InboxPageElements.LOGOUT_BUTTON).click()
