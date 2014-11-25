#coding:utf-8

'''
module::codes
~~~~~~~~~~~~~~~
Get & Verify Codes
'''


from requests import Request
from g_common import API_URL, render_url


def get_code(phone):
    request_body = {'phone': phone}
    return Request("POST", render_url('/codes'), data=request_body)

def verify_code(phone, code):
    request_body = {'phone': phone, 'code': code}
    return Request("POST", render_url('/codes'), data=request_body)
