#coding:utf-8

'''
module::login
~~~~~~~~~~~~~~~
'''

from requests import Request


API_URL = "http://api.gizwits.com/app"

def render_url(url):
    return API_URL + url

def login(acc, pwd):
    request_body = {'username': acc, 'password': pwd}
    return Request("POST", render_url('/login'), data=request_body)
