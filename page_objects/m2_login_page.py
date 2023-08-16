from seleniumbase import BaseCase

from page_objects.basepage import BasePage
from testdata_folder.config import TestData


class LoginPage(BasePage):

    def setUp(self):
        super().setUp()
        print('setup method')
        # self.open(TestData.URL_magento)
        self.maximize_window()

    def tearDown(self):
        print('tear down method')
        super().tearDown()

    def open_magento_site(self):
        self.open(TestData.URL_magento)