import requests
import json
import logging

from api.client import APIClient
from calls import g_users, g_login, g_codes, g_device

def auto_token(func):
    def _auto_token(*args, **kwargs):
        client_obj = args[0]    # like self
        resp = func(*args, **kwargs)
        d = resp.json()
        client_obj = client_obj.set_token(d.get('token', 'ERROR'))
        logging.debug('token:%s'%client_obj.token)
        return resp
    return _auto_token

class GServiceClient(APIClient):

    def __init__(self, appid):
	APIClient.__init__(self)
	self.headers.update({
		'X-Gizwits-Application-Id': appid,
		})
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
        r = g_users.anonymous_login(phone_id)
        return self.send_request(r)


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
        r = g_device.bind_devices(devices)
        return self.send_request(r)


    def control_device(self, did, raw):
	'''
	:param did: did
	:type did: String

	:param raw: struct => [<byte>, <byte>, ...]
	:type raw: list

        '''
        r = g_device.remote_control_device(did, raw)
        return self.send_request(r)


    def get_bind_device(limit=20, skip=0):
	return self.send_request(g_device.get_bound_devices(limit, skip))
