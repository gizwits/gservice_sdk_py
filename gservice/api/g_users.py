#coding:utf-8

'''
module::Users
~~~~~~~~~~~~~~~
'''

from requests import Request


API_URL = "http://api.gizwits.com/app"

def render_url(url):
    return API_URL + url

def create_user_by_username(username, password):
    request_body = {'username': username,
                    'password': password}
    return Request("POST", render_url('/users'), data=request_body)

def create_user_by_email(self, email, password):
    request_body = {'email': username,
                    'password': password}
    return Request("POST", render_url('/users'), data=request_body)

def create_user_by_phone(self, phone, password, code):
    request_body = {'phone': phone,
                    'password': password,
                    'code': code
                    }
    return Request("POST", render_url('/users'), data=request_body)

def anonymous_login(self, phone_id):
    request_body = {'phone_id': phone_id}
    return Request("POST", render_url('/users'), data=request_body)

def update_user_info(self, username, password):
    request_body = {'username': username, 'password': password}
    return Request("PUT", render_url('/users'), data=request_body)

def update_info(self, username, password):
    request_body = {'username': username, 'password': password}
    return Request("PUT", render_url('/users'), data=request_body)

def update_pwd(self, old_pwd, new_pwd):
    request_body = {
        "old_pwd": old_pwd,
        "new_pwd": new_pwd
        }
     return Request("PUT", render_url('/users'), data=request_body)

def update_email(self, email):
    request_body = {
        "email": "bob@bob.com",
        }
    return Request("PUT", render_url('/users'), data=request_body)

def update_phone_code(self, phone, code):
    request_body = {
        "phone": "1328830223",
        "code": "abc"
        }
    return Request("PUT", render_url('/users'), data=request_body)

def request_password_reset(self, email):
    # todo:reset password
    pass
