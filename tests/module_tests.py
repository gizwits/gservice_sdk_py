#coding:utf-8


import unittest
from gservice.calls import g_users, g_device, g_login, g_codes, g_common


class TestRequest(unittest.TestCase):
    '''
    just test request object.
    '''
    def setUp(self):
        pass

    def _http_GET(self, test):
        self.assertEquals(test, "GET")

    def _http_POST(self, test):
        self.assertEquals(test, "POST")

    def _http_DELETE(self, test):
        self.assertEquals(test, "DELETE")

    def _http_PUT(self, test):
        self.assertEquals(test, "PUT")

    def test_object(self):
        user_url = g_common.API_URL + '/users'
        req = g_users.create_user_by_username('','')
        self._http_POST(req.method)
        self.assertEquals(req.url, user_url)

        req = g_users.create_user_by_email('','')
        self._http_POST(req.method)
        self.assertEquals(req.url, user_url)

        req = g_users.create_user_by_phone('','','')
        self._http_POST(req.method)
        self.assertEquals(req.url, user_url)

        req = g_users.anonymous_login('')
        self._http_POST(req.method)
        self.assertEquals(req.url, user_url)

        req = g_users.create_user_by_auth_data({})
        self._http_POST(req.method)
        self.assertEquals(req.url, user_url)

        #update user info
        req = g_users.update_info('', '')
        self._http_PUT(req.method)
        self.assertEquals(req.url, user_url)

        req = g_users.update_pwd('', '')
        self._http_PUT(req.method)
        self.assertEquals(req.url, user_url)

        req = g_users.update_email('')
        self._http_PUT(req.method)
        self.assertEquals(req.url, user_url)

        req = g_users.update_phone_code('','')
        self._http_PUT(req.method)
        self.assertEquals(req.url, user_url)

        req = g_users.update_phone_pwd_code('','', '')
        self._http_PUT(req.method)
        self.assertEquals(req.url, user_url)
        
        # reset password
        reset_url = 'http://api.gizwits.com/app/reset_password'
        req = g_users.password_reset('')
        self._http_PUT(req.method)
        self.assertEquals(req.url, reset_url)

        # login
        login_url = 'http://api.gizwits.com/app/login'
        req = g_login.login('','')
        self._http_POST(req.method)
        self.assertEquals(req.url, login_url)

        # codes
        codes_url = 'http://api.gizwits.com/app/codes'
        req = g_codes.get_code('')
        self._http_POST(req.method)
        self.assertEquals(req.url, codes_url)

        req = g_codes.verify_code('', '')
        self._http_POST(req.method)
        self.assertEquals(req.url, codes_url)


if __name__ == '__main__':
    unittest.main()
