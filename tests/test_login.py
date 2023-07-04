from pages.Login_page import Login_page


class Login(Login_page):
    login = Login_page()


    def test_url(self):
        self.login.verify_login_url()

    def test_page_title(self):
        self.login.verify_page_title()

    def test_login_header_text(self):
        self.login.verify_login_header_text()

    def test_login_button_displayed(self):
        self.login.verify_login_button_displayed()

    def test_error_message_login(self):
        self.login.verify_error_message_login()

    def test_login_success(self):
        self.login.verify_login_success()

    def test_verify_login_logout(self):
        self.login.verify_login_logout()





