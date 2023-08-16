from page_objects import Page
from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://demo.imagility.co/login/login/signin")
        self.assert_exact_text("", Page.css_1)
        self.click(Page.css_2)
        self.click(Page.css_3)
        self.click(Page.css_4)
        self.click(Page.css_5)
        self.click(Page.css_6)
        self.type(Page.css_7, "prasad")
        self.type(Page.css_8, "teeet")
        self.click(Page.css_9)
        self.type(Page.css_10, "india\n")
        self.click(Page.css_9)
        self.click(Page.css_11)
        self.type(Page.css_12, "9000900098")
        self.type(Page.css_13, "testlkjkki@gmail.com")
        self.type(Page.css_14, "Test123$")
        self.type(Page.css_15, "Test123$")
        self.click(Page.css_16)
        self.click(Page.css_4)
        self.click(Page.css_17)
