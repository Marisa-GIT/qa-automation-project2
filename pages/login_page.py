from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "#submit"
        self.error_message = "#error"

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)
    
    def get_error_message(self):
        return self.page.inner_text(self.error_message)
    
    def get_error_message(self):
        return self.page.locator("#error").inner_text()
