from seleniumbase import BaseCase

from testdata_folder.config import TestData


class BasePage(BaseCase):

    def setUp(self):
        super().setUp()
        # self.open(TestData.URL_magento)
        self.maximize_window()

    def tearDown(self):
        super().tearDown()

    def open_magento_site(self):
        self.open(TestData.URL_magento)

    def open_imagility_site(self):
        self.open(TestData.URL_imagility)

    def open_JDE_site(self):
        self.open(TestData.URL_JDE)