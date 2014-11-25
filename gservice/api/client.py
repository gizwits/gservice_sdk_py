#coding:utf-8

'''
moduls::APIClient
~~~~~~~~~~~~~~~~~
request handler
'''

import requests
import json

from ..calls.g_login import login as login_call

class APIClient(object):

    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.uid = None
        self.expire_at = None
        self.headers = {"Content-Type": "application/json"}

    def set_token(self, token):
        '''Set token manually to avoid having to login repeatedly'''
        self.token = token
        self.headers["X-Gizwits-User-token"] = self.token
    
    def login(self, acc, pwd):
        '''login to gservice
        '''
        r = self.send_request(login_call(acc, pwd))
        self.set_token(r['token'])
        self.uid = r['uid']
        self.expire_at = r['expire_at']

    def send_request(self, request, timeout=30):
        '''
        :param request: A prepared Request object for the request.
        :type request_method: Request
        :param timeout: Timeout duration in seconds.
        :type timeout: int
        :returns: dict
        '''
        request.headers = self.headers
        # Include the session headers in the request
        request.headers.update(self.session.headers)
        if request.data == []:
            request.data = json.dumps({})
        else:
            request.data = json.dumps(request.data)

        r = self.session.send(request.prepare(), timeout=timeout)

        if r.status_code < 300:
            return r.json()
        elif r.status_code == 404:  # dirty hack around this timing bullshit
            time.sleep(1)
            r2 = self.session.send(request.prepare(), timeout=timeout)
            if r2.status_code == 404:  # still doesn't work
                raise Exception(r2.status_code, r2)
            else:
                return r2.json()
        else:
            raise Exception(r.status_code, r)
