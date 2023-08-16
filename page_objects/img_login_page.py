from seleniumbase import BaseCase

from page_objects.basepage import BasePage


class LoginPage(BasePage):
    login_register_btn = "//a[contains(text(), 'Register')]"
    forSelf_cb = 'p-radiobutton[name="type"] div:nth-of-type(2)'
    proceed_btn = 'button[title="Proceed"]'
    title_dd = 'p-dropdown[name="title"] span'
    title_option = 'p-dropdown[name="title"] div:nth-of-type(3) ul p-dropdownitem:nth-of-type(2) li div'
    firstname = 'input[placeholder="First Name"]'
    lastname = 'input[placeholder="Last Name"]'
    phone_dd = 'p-dropdown[name="visatype"] div:nth-of-type(2)'
    phone_search = 'p-dropdown[name="visatype"] div:nth-of-type(3) div input'
    phone_option = 'li:contains("India - 91")'
    phone = 'input[name="phone"]'
    email = 'input[placeholder="Email "]'
    password = 'input[placeholder="Password"]'
    confirm_password = 'input[placeholder="Confirm Password"]'
    terms_and_conditions = "span.mat-checkbox-inner-container"
    next = "button[title='Proceed']"

    def click_on_registor_btn(self):
        self.assert_text('REGISTER', self.login_register_btn)
        self.click(self.login_register_btn)

    def fill_register_form(self):
        self.assert_text("WELCOME !", 'h4')
        self.click(self.forSelf_cb)
        self.click(self.proceed_btn)

        self.assert_text("Let us know the personal details", "//h5")
        self.click(self.title_dd)
        self.click(self.title_option)
        self.type(self.firstname, 'automation')
        self.type(self.lastname, 'test')

        self.click(self.phone_dd)
        self.type(self.phone_search, 'India')
        self.click(self.phone_option)
        self.type(self.phone, '9000900090')

        self.type(self.email, 'automationtest123@mailinator.com')
        self.type(self.password, 'Test123$')
        self.type(self.confirm_password, 'Test123$')

        self.click(self.terms_and_conditions)
        self.sleep(3)
        # self.click(self.next)
