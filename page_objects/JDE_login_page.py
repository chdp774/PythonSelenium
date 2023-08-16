from seleniumbase import BaseCase

from page_objects.basepage import BasePage
from testdata_folder.config import TestData as data


class JDETest(BasePage):

    JDE_username = 'input#User'
    JDE_password = 'input#Password'
    JDE_login_btn = 'input[value="Sign In"]'
    JDE_logo = '#appName'

    def do_login(self):
        self.assert_title(data.JDE_title)
        self.assertTrue(self.JDE_logo)
        # self.assert_text(self.JDE_logo, data.JDE_title)
        self.type(self.JDE_username, data.JDE_username)
        self.type(self.JDE_password, data.JDE_password)
        self.click(self.JDE_login_btn)
        # self.assert_title('')