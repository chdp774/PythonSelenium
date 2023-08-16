from seleniumbase import BaseCase

from page_objects.basepage import BasePage
from page_objects.img_login_page import LoginPage


class RegisterTest(LoginPage):

    def test_imagility(self):
        self.open_imagility_site()
        self.click_on_registor_btn()
        self.fill_register_form()
