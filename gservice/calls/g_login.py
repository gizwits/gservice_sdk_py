#coding:utf-8

'''
module::login
~~~~~~~~~~~~~~~
'''

from requests import Request
from g_common import API_URL, render_url


def login(acc, pwd):
    request_body = {'username': acc, 'password': pwd}
    return Request("POST", render_url('/login'), data=request_body)
