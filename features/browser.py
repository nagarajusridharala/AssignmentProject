from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome("C:\\work\\UIWorkSpace\\ecart\\src\\test\\resources\\drivers\\chromedriver.exe")
    driver.implicitly_wait(30)
    # driver.get('http://automationpractice.com/index.php')
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(self):
        self.driver.quit()
