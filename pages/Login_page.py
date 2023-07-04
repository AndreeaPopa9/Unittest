
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import base_page

class Login_page(base_page.Base_page):

    email = 'andreeapopa9793@gmail.com'
    password = 'ConstantlyLearn9*'
    LOGIN_PAGE = (By.XPATH, "//a[text()='Log In']")
    LOGIN_HEADER_TEXT = (By.XPATH, "//div[@class='little-big-header']")
    EMAIL_FIELD = (By.ID, "login-email-field")
    PASSWORD_FIELD = (By.ID, "login-password-field")
    LOGIN_BUTTON = (By.ID, "log-in-button")
    MESSAGE_ERROR = (By.XPATH, "//*[@id='login-email']/div")
    USER_MENU_BTN = (By.XPATH, "//div[@id='react-page']/div/nav/button")
    LOGOUT_BTN = (By.XPATH, "//*[@class='DropdownControlled-module_content-mxnG0']/div/button[3]")


    def verify_login_url(self):
        actual = self.chrome.current_url
        expected = 'https://codepen.io/login'
        self.assertEqual(expected, actual, 'URL is not correct')

    def verify_page_title(self):
        actual = self.chrome.title
        expected = 'CodePen Login'
        self.assertEqual(expected, actual, f'Title page is {actual}, but it should be {expected}')

    def verify_login_header_text(self):
        actual = self.chrome.find_element(*self.LOGIN_HEADER_TEXT).text
        expected = "Log In"
        self.assertEqual(expected, actual, f'The text on the header is {actual}, but it should be {expected}')

    def verify_login_button_displayed(self):
        button = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(button.is_displayed(), "Login button is not displayed.")

    def verify_error_message_login(self):
        self.chrome.find_element(*self.EMAIL_FIELD).send_keys("andreeapopa9793")
        self.chrome.find_element(*self.PASSWORD_FIELD).send_keys("ConstantlyLearn9*")
        element = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.chrome.execute_script("arguments[0].click();", element)
        #actual = self.chrome.find_element(*self.MESSAGE_ERROR).text
        #expected = "The username or password you entered is incorrect, please try again."
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.MESSAGE_ERROR))
        #self.assertTrue(expected in actual, "Error text message is incorrect.")
        assert self.chrome.find_element(*self.MESSAGE_ERROR).is_displayed() == True


    def verify_login_success(self):
        self.chrome.find_element(*self.EMAIL_FIELD).send_keys("andreeapopa9793@gmail.com")
        self.chrome.find_element(*self.PASSWORD_FIELD).send_keys("ConstantlyLearn9*")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        expected_page_title = "Following - CodePen"
        WebDriverWait(self.chrome, 10).until(EC.title_contains(expected_page_title))
        self.assertIn(expected_page_title, self.chrome.title)


    def verify_login_logout(self):
        self.chrome.find_element(*self.EMAIL_FIELD).send_keys("andreeapopa9793@gmail.com")
        self.chrome.find_element(*self.PASSWORD_FIELD).send_keys("ConstantlyLearn9*")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.USER_MENU_BTN).click()
        self.chrome.find_element(self.LOGOUT_BTN).click()
        actual_url = self.chrome.current_url
        expected_url = "https://codepen.io/"
        assert actual_url == expected_url, f'Invalid URL: {actual_url} is different of {expected_url}'







