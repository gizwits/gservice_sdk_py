#coding:utf-8

'''
module::Users
~~~~~~~~~~~~~~~

todo: update_ need ``X-Gizwits-User-token: {token}``
'''


from requests import Request
from g_common import API_URL, render_url

def create_user_by_username(username, password):
    request_body = {'username': username,
                    'password': password}
    return Request("POST", render_url('/users'), data=request_body)

def create_user_by_email(email, password):
    request_body = {'email': email,
                    'password': password}
    return Request("POST", render_url('/users'), data=request_body)

def create_user_by_phone(phone, password, code):
    request_body = {'phone': phone,
                    'password': password,
                    'code': code
                    }
    return Request("POST", render_url('/users'), data=request_body)

def create_user_by_auth_data(auth_data):
    '''
    :param auth_data: struct => {'src':'baidu|sina|qq', 'uid':'2346677','token':'pnktnjyb996sj4p156gjtp4im'}
    :type: dict
    '''
    request_body = {'authData': auth_data}
    return Request("POST", render_url('/users'), data=request_body)

def anonymous_login(phone_id):
    request_body = {'phone_id': phone_id}
    return Request("POST", render_url('/users'), data=request_body)

def update_info(username, password):
    request_body = {'username': username, 'password': password}
    return Request("PUT", render_url('/users'), data=request_body)

def update_pwd(old_pwd, new_pwd):
    request_body = {
        "old_pwd": str(old_pwd),
        "new_pwd": str(new_pwd)
        }
    return Request("PUT", render_url('/users'), data=request_body)

def update_email(email):
    request_body = {
        "email": str(email)
        }
    return Request("PUT", render_url('/users'), data=request_body)

def update_phone_code(phone, code):
    request_body = {
        "phone": str(phone),
        "code": str(code)
        }
    return Request("PUT", render_url('/users'), data=request_body)

def update_phone_pwd_code(phone, pwd, code):
    request_body = {
        "phone": str(phone),
        "password": str(pwd),
        "code": str(pwd)
        }
    return Request("PUT", render_url('/users'), data=request_body)

def password_reset(email):
    request_body = {
        "email": email
        }
    return Request("POST", render_url('/reset_password'), data=request_body)

def password_reset_with(phone, code, new_pwd):
    request_body = {
        "phone": phone,
        "code": code,
        "new_pwd": new_pwd
        }
    return Request("PUT", render_url('/reset_password'), data=request_body)
