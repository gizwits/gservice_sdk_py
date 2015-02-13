
'''
    GService SDK Client
    ~~~~~~~~~~~~~~~~~~~

    document center: http://site.gizwits.com/document/m2m/openapi/
'''
import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG)

from api.client import APIClient
from calls import g_users, g_login, g_codes, g_device

def auto_token(func):
    def _auto_token(*args, **kwargs):
        client_obj = args[0]    # like self
        resp = func(*args, **kwargs)
        d = resp.json()
        try:
            _token = d['token']
            client_obj = client_obj.set_token(_token)
        except KeyError:
            # ensure your request can get the token
            pass
        return resp
    return _auto_token

class GServiceClient(APIClient):

    def __init__(self, appid):
        APIClient.__init__(self)
        self.headers.update({
                'X-Gizwits-Application-Id': appid,
                })

    # ===user
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

    # update
    def update_info(self, username, password):
        r = g_users.update_info(username, password)
        return self.send_request(r)

    def update_pwd(self, old_pwd, new_pwd):
        r = g_users.update_pwd(old_pwd, new_pwd)
        return self.send_request(r)

    def update_email(self, email):
        r = g_users.update_email(email)
        return self.send_request(r)

    def update_phone_code(self, phone, code):
        r = g_users.update_phone_code(phone, code)
        return self.send_request(r)

    def update_phone_pwd_code(self, phone, pwd, code):
        r = g_users.update_phone_pwd_code(phone, pwd, code)
        return self.send_request(r)

    # password reset
    def password_reset(self, email):
        r = g_users.password_reset(email)
        return self.send_request(r)

    def password_reset_with(self, phone, code, new_pwd):
        r = g_users.password_reset_with(phone, code, new_pwd)
        return self.send_request(r)

    #===codes
    def get_code(self, phone):
        r = g_codes.get_code(phone)
        return self.send_request(r)

    def verify_code(self, phone, code):
        r = g_codes.verify_code(phone, code)
        return self.send_request(r)

    # === device
    def retrieve_device_histroy_data(self, did, start_ts=None,
                                     end_ts=None, entity=None,
                                     attr=None, limit=20,
                                     skip=0):
        r = g_device.retrieve_device_histroy_data(did,
                                                  start_ts,
                                                  end_ts,
                                                  entity,
                                                  attr,
                                                  limit,
                                                  skip
                                                  )
        return self.send_request(r)

    def retrieve_product_histroy_data(self, product_key, did=None,
                                      start_ts=None, end_ts=None,
                                      entity=None, attr=None,
                                      limit=20, skip=0):
        r = g_device.retrieve_product_histroy_data(product_key,
                                          did,
                                          start_ts,
                                          end_ts,
                                          entity,
                                          attr,
                                          limit,
                                          skip
                                          )
        return self.send_request(r)

    # bound device
    def bind_device(self, devices):
        '''
        :param devices: struct = > [('did', 'passcode', 'remark(optional)', ...]
        :returns: Response
        '''
        r = g_device.bind_devices(devices)
        return self.send_request(r)

    def unbind_devices(self, devices):
        '''
        :param devices: struct = > [('did', 'passcode'), ...]
        '''
        r = g_device.unbind_devices(devices)
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

    def get_bind_device(self, limit=20, skip=0):
        return self.send_request(g_device.get_bound_devices(limit, skip))


    # device detail
    def device_detail(self, did):
        r = g_device.device_detail(did)
        return self.send_request(r)
    
    def query_device(self, product_key, mac):
        r = g_device.query_device(product_key, mac)
        return self.send_request(r)

    def remote_control_device(self, did, raw):
        '''
        :param did: did
        :type did: String

        :param raw: struct => [<byte>, <byte>, ...]
        :type raw: list
        '''
        r = g_device.remote_control_device(did, raw)
        return self.send_request(r)

    def create_scheduler(self, time, repeat, retry_count, retry_task, tasks, date=None):
        '''
        http://site.gizwits.com/document/m2m/openapi/#appschedulerlimitskip
        :param date: required if repeat is 'none'
        '''
        r = g_device.create_scheduler(date, time, repeat, retry_count, retry_task, tasks)
        resp = self.send_request(r)
        logging.debug(resp.content)
        return resp

    def fetch_scheduler(self, skip=None, limit=None):
        '''
        http://site.gizwits.com/document/m2m/openapi/#get_4
        '''
        r = g_device.fetch_scheduler(skip, limit)
        resp = self.send_request(r)
        logging.debug(resp.content)
        return resp

    def del_scheduler(self, sid):
        '''
        http://site.gizwits.com/document/m2m/openapi/#delete_1
        '''
        r = g_device.del_scheduler(sid)
        resp = self.send_request(r)
        logging.debug(resp.content)
        return resp

    def scheduler_logs(self, sid):
        '''
        http://site.gizwits.com/document/m2m/openapi/#get_5
        '''
        r = g_device.scheduler_logs(sid)
        resp = self.send_request(r)
        logging.debug(resp.content)
        return resp
