from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)


class RecorderTest(BaseCase):
    def test_recording(self):
        self.open("https://qa900.na.atriumcorp.local/jde/E1Menu.maf?jdeowpBackButtonProtect=PROTECTED")
        self.type("input#User", "&")
        self.type("input#User", "pchippada")
        self.type("input#Password", "Trading@20234")
        self.click('input[value="Sign In"]')
        self.open("https://qa900.na.atriumcorp.local/jde/E1Menu.maf?jdeowpBackButtonProtect=PROTECTED")
        self.click("div#drop_mainmenu")
        self.click("span#fldnode405495")
        self.click("span#fldnode405507")
        self.click("a#fldnode405567")
        self.switch_to_frame("iframe#e1menuAppIframe")
