import time
from selenium.webdriver.common.by import By


class RevHousePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://www.revhouse.io/'
        self.browser.get(self.url)

    def is_display(self):
        return self.browser.find_element(By.CLASS_NAME, 'logo-section')

    def button_main_image(self):
        return self.browser.find_element(By.CLASS_NAME, 'chevron').click()

    def id_culture(self):
        return self.browser.find_element(By.ID, 'culture')

    def click_mission(self):
        return self.browser.find_element(By.LINK_TEXT, 'OUR MISSION').click()

    def click_services(self):
        return self.browser.find_element(By.LINK_TEXT, 'SERVICES').click()

    def click_contact(self):
        return self.browser.find_element(By.LINK_TEXT, 'CONTACT').click()

    def select_service(self):
        button = self.browser.find_element(By.ID, 'web-basic')
        # button = self.browser.find_element(By.ID, 'web-corporative')
        # button = self.browser.find_element(By.ID, 'web-customize')
        # button = self.browser.find_element(By.ID, 'qa-basic')
        # button = self.browser.find_element(By.ID, 'qa-corporative')
        # button = self.browser.find_element(By.ID, 'qa-customize')
        # button = self.browser.find_element(By.NAME, 'I want the data analysis plan')
        # button = self.browser.find_element(By.NAME, 'I want the data analysis + data engineering plan')
        # button = self.browser.find_element(By.NAME, 'I want the data driven plan')
        self.browser.execute_script("arguments[0].click();", button)
        return self.browser.execute_script("window.scrollTo(0, 0)")  # Up scroll

    def click_image_nav(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        return self.browser.find_element(By.CLASS_NAME, 'navbar-logo').click()

    def complete_form(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        name = self.browser.find_element(By.ID, 'user_name')
        name.send_keys('Rodrigo')
        email = self.browser.find_element(By.ID, 'user_email')
        email.send_keys('rodri@salas.com')
        message = self.browser.find_element(By.ID, 'message')
        message.send_keys('Test')
        button = self.browser.find_element(By.CLASS_NAME, "button")
        return self.browser.execute_script("arguments[0].click();", button)

    def message_ok(self):
        return self.browser.find_element(By.ID, 'swal2-html-container')

    def complete_form_name_with_numbers(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        name = self.browser.find_element(By.ID, 'user_name')
        name.send_keys('111')
        email = self.browser.find_element(By.ID, 'user_email')
        email.send_keys('rodri@salas.com')
        message = self.browser.find_element(By.ID, 'message')
        message.send_keys('Test')
        button = self.browser.find_element(By.CLASS_NAME, "button")
        return self.browser.execute_script("arguments[0].click();", button)

    def complete_form_email_without_at(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        name = self.browser.find_element(By.ID, 'user_name')
        name.send_keys('Rodrigo')
        email = self.browser.find_element(By.ID, 'user_email')
        email.send_keys('rodri111salas.com')
        message = self.browser.find_element(By.ID, 'message')
        message.send_keys('Test')
        button = self.browser.find_element(By.CLASS_NAME, "button")
        return self.browser.execute_script("arguments[0].click();", button)