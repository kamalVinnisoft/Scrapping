

from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

class TestSimpleLogin(BaseCase):
    def test_simple_login(self):
        self.open("https://in.linkedin.com/")
        self.click('a.nav__button-secondary')
        self.type("#username", "kamalpreetvinni@gmail.com")
        self.type("#password", "Kamal@123")
        self.click('button.btn__primary--large')
        # self.assert_element("img#image1")
        # self.highlight("#image1")
        self.sleep(122)