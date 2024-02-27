from PageObjects.LoginObj.login_ismart import LoginIsmart


class Test_Login(LoginIsmart):

    def test_login_using_valid_cred(self):
        self.login_to_ismart_application()
