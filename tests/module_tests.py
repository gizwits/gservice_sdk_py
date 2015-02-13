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
        self._http_POST(req.method)
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

        # devices
        device_data_did = 'tests'
        req = g_device.retrieve_device_histroy_data(device_data_did)
        self._http_GET(req.method)
        self.assertEquals(req.url, 'http://api.gizwits.com/app/devdata/' + device_data_did)

        device_data_url = 'http://api.gizwits.com/app/devdata'
        device_data_product_key = 'test_pk'
        req = g_device.retrieve_product_histroy_data(device_data_product_key)
        self._http_GET(req.method)
        self.assertEquals(req.url, device_data_url)

        # bound
        bound_url = 'http://api.gizwits.com/app/bindings'
        req = g_device.get_bound_devices('')
        self._http_GET(req.method)
        self.assertEquals(req.url, bound_url)
        
        req = g_device.bind_devices([])
        self._http_POST(req.method)
        self.assertEquals(req.url, bound_url)

        req = g_device.unbind_devices([])
        self._http_DELETE(req.method)
        self.assertEquals(req.url, bound_url)

        # device
        device_detail_did = 'test_did'
        device_detail_url = 'http://api.gizwits.com/app/devices/' + device_detail_did
        req = g_device.device_detail(device_detail_did)
        self._http_GET(req.method)
        self.assertEquals(req.url, device_detail_url)

        req = g_device.query_device('','')
        self._http_GET(req.method)
        self.assertEquals(req.url, 'http://api.gizwits.com/app/devices')

        # control
        control_did = 'test_did'
        control_url = 'http://api.gizwits.com/app/control/' + control_did
        req = g_device.remote_control_device(control_did, [])
        self._http_POST(req.method)
        self.assertEquals(req.url, control_url)

        # scheduler
        control_did = 'test_did'
        scheduler_url = 'http://api.gizwits.com/app/scheduler'
        req = g_device.create_scheduler('', '', '', '', '', '')
        self._http_POST(req.method)
        self.assertEquals(req.url, scheduler_url)

        # scheduler
        control_did = 'test_did'
        scheduler_url = 'http://api.gizwits.com/app/scheduler'
        req = g_device.fetch_scheduler('', '')
        self._http_GET(req.method)
        self.assertEquals(req.url, scheduler_url)

        # scheduler
        control_did = 'test_did'
        _id = 'asdf'
        scheduler_url = 'http://api.gizwits.com/app/scheduler/{0}'.format(_id)
        req = g_device.del_scheduler(_id)
        self._http_DELETE(req.method)
        self.assertEquals(req.url, scheduler_url)

        # scheduler
        control_did = 'test_did'
        _id = 'asdf'
        scheduler_url = 'http://api.gizwits.com/app/scheduler/{0}/logs'.format(_id)
        req = g_device.scheduler_logs(_id)
        self._http_GET(req.method)
        self.assertEquals(req.url, scheduler_url)


if __name__ == '__main__':
    unittest.main()
