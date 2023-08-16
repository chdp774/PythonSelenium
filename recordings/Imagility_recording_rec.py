from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://demo.imagility.co/login/login/signin")
        self.assert_exact_text("", 'img[src="../../../../assets/weblogo.png"]')
        self.click('a[href="/login/registerImmigrantType"]')
        self.click('p-radiobutton[name="type"] div:nth-of-type(2)')
        self.click('button[title="Proceed"]')
        self.click('p-dropdown[name="title"] span')
        self.click('p-dropdown[name="title"] div:nth-of-type(3) ul p-dropdownitem:nth-of-type(2) li div')
        self.type('input[placeholder="First Name"]', "prasad")
        self.type('input[placeholder="Last Name"]', "teeet")
        self.click('p-dropdown[name="visatype"] div:nth-of-type(2)')
        self.type('p-dropdown[name="visatype"] div:nth-of-type(3) div input', "india\n")
        self.click('p-dropdown[name="visatype"] div:nth-of-type(2)')
        self.click('li:contains("India - 91")')
        self.type('input[name="phone"]', "9000900098")
        self.type('input[placeholder="Email "]', "testlkjkki@gmail.com")
        self.type('input[placeholder="Password"]', "Test123$")
        self.type('input[placeholder="Confirm Password"]', "Test123$")
        self.click("span.mat-checkbox-inner-container")
        self.click('button[title="Proceed"]')
        self.click('p-radiobutton[label="No"] div:nth-of-type(2)')
