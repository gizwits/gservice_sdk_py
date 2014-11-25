import requests
import json
import logging

from api.client import APIClient
from calls import g_users, g_login, g_codes, g_device

def auto_token(func):
    def _auto_token(*args, **kwargs):
        client_obj = args[0]    # like self
        d = func(*args, **kwargs)
        client_obj = client_obj.set_token(d.get('token', 'ERROR'))
        logging.debug('token:%s'%client_obj.token)
        return d
    return _auto_token

class GServiceClient(APIClient):

    URL = 'http://api.gizwits.com/app'

    def __init__(self, appid):
        APIClient.__init__(self)
        self.headers.update({
                'X-Gizwits-Application-Id': appid,
                })

    def get_url(self, url):
        return GServiceClient.URL + url

    @auto_token
    def create_user_by_username(self, username, password):
        r = g_users.create_user_by_username(username, password)
        return self.send_request(r)

    @auto_token
    def create_user_by_email(self, email, password):
        r = g_users.create_user_by_email(email, password)
        return self.send_request(r)

    @auto_token
    def create_user_by_phone(self, phone, password, code):
        r = g_users.create_user_by_phone(phone, password, code)
        return self.send_request(r)

    @auto_token
    def anonymous_login(self, phone_id):
        url = self.get_url('/users')
        data = {'phone_id': phone_id}
        return self.client.post(url, data=json.dumps(data))

    @auto_token
    def _login(self, username, password):
        r = g_login.login(username, password)
        return self.send_request(r)

    @auto_token
    def login_by_username(self, username, password):
        return self._login(username, password)

    @auto_token
    def login_by_email(self, email, password):
        return self._login(email, password)

    @auto_token
    def login_by_phone(self, phone, password):
        return self._login(phone, password)
    
    def get_code(self, phone):
        r = g_codes.get_code(phone, password, code)
        return self.send_request(r)

    def verify_code(self, phone, code):
        r = g_codes.verify_code(phone, code)
        return self.send_request(r)

    def bind_device(self, devices):
        '''
        :param devices: struct = > [('did', 'passcode'), ...]
        :returns: Response
        '''
        url = self.get_url('/bindings')
        data_devices = []
        for did, passcode in devices:
            device = {'did': None, 'passcode': None}
            device['did'] = did
            device['passcode'] = passcode
            data_devices.append(device)
        data = {'devices':data_devices}
        self.client.headers.update({'X-Gizwits-User-token': self.token})
        return self.client.post(url, data=json.dumps(data))

    def control_device(self, did, raw):
        '''
        :param did: did
        :type did: String

        :param raw: struct => [<byte>, <byte>, ...]
        :type raw: list

        :returns: Response
        '''
        data = {'raw': raw}
        url = self.get_url('/control')
        url = url + '/' + str(did)
        self.client.headers.update({'X-Gizwits-User-token': self.token})
        return self.client.post(url, data=json.dumps(data))

    def get_bind_device(limit=20, skip=0):
        return self.send_request(g_device.get_bound_devices(limit, skip))
