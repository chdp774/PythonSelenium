from page_objects.m2_login_page import LoginPage
from testdata_folder.config import TestData


class MagentoTest(LoginPage):
    def test_magento(self):
        self.open_magento_site()
        self.type('#username', TestData.M2_username)
        self.type('#login', TestData.M2_password)
        self.click("//span[contains(text(), 'Sign in')]")
        self.assert_title('Dashboard / Magento Admin')
        self.sleep(5)
        self.click('#menu-magento-customer-customer', timeout=30)  # Menu - Customers
        self.sleep(5)
        self.click('.item-customer-manage', timeout=10)  # Menu - All customers
        # try:
        #     print('Try block')
        #     self.click(".admin__data-grid-header button[data-bind *= 'Clear all']")
        #     self.type("//input[text() = 'Search by keyword']", '85060287\n', timeout=30)
        #     # self.sleep(10)
        # except:
        #     print('Catch block')
        #     self.type("//input[text() = 'Search by keyword']", '85060287\n', timeout=30)
        #     # self.sleep(10)
        #
        # self.click("//a[text() = 'Edit']")  # Edit
        # self.click('#order', timeout=30)
        # self.click("label[for = 'store_1']", timeout=30)
        # self.click("//span[contains(text(), 'Add Products By SKU')]/parent::button", timeout=30)
        # self.type('#sku_0', 'VD16')
        # self.type('#sku_qty_0', '5')
        # self.click("button[title='Add to Order']", timeout=30)
        # self.click("#order-shipping-method-summary", timeout=30)

        # self.click("label[for='s_method_freeshipping_freeshipping']", timeout=10)
        # self.click('#submit_order_top_button')  # submit button