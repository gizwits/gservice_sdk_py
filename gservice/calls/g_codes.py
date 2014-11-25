#coding:utf-8

'''
module::codes
~~~~~~~~~~~~~~~
Get & Verify Codes
'''

from requests import Request


API_URL = "http://api.gizwits.com/app"

def render_url(url):
    return API_URL + url

def get_code(self, phone):
    request_body = {'phone': phone}
    return Request("POST", render_url('/codes'), data=request_body)

def verify_code(self, phone, code):
    request_body = {'phone': phone, 'code': code}
    return Request("POST", render_url('/codes'), data=request_body)
