from Page.page_address import PageAddress
from Page.page_login import PageLogin
from Base.get_driver import get_driver


class PageIn():

    def __init__(self):
        self.driver = get_driver()

    def page_get_login(self):
        return PageLogin(self.driver)

    def page_get_address(self):
        return PageAddress(self.driver)
