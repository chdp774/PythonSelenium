from page_objects.JDE_login_page import JDETest
from testdata_folder.config import TestData


class JDETest(JDETest):
    def test_JDE(self):
        self.open_JDE_site()
        self.do_login()
