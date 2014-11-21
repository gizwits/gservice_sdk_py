import requests
import json


class GServiceClient(object):

    URL = 'http://api.gizwits.com/app'
    
    def __init__(self, appid):
        self.client = requests.Session()
        self.client.headers.update({
                'X-Gizwits-Application-Id': appid,
                'Content-Type': 'application/json'})

    def get_url(self, url):
        return GServiceClient.URL + url

    def create_user_by_username(self, username, password):
        url = self.get_url('/users')
        data = {'username': username,
                'password': password}
        return self.client.post(url, data=json.dumps(data))

    def create_user_by_email(self, email, password):
        url = self.get_url('/users')
        data = {'email': email,
                'password': password}
        return self.client.post(url, data=json.dumps(data))

    def create_user_by_phone(self, phone, password, code):
        url = self.get_url('/users')
        data = {'phone': phone,
                'password': password,
                'code': code}
        return self.client.post(url, data=json.dumps(data))

    def anonymous_login(self, phone_id):
        url = self.get_url('/users')
        data = {'phone_id': phone_id}
        return self.client.post(url, data=json.dumps(data))

    def _login(self, username, password):
        url = self.get_url('/login')
        data = {'username': username,
                'password': password}
        return self.client.post(url, data=json.dumps(data))

    def login_by_username(self, username, password):
        return self._login(username, password)

    def login_by_email(self, email, password):
        return self._login(email, password)

    def login_by_phone(self, phone, password):
        return self._login(phone, password)

    def get_code(self, phone):
        url = self.get_url('/codes')
        data = {'phone': phone}
        return self.client.post(url, data=json.dumps(data))

    def verify_code(self, phone, code):
        url = self.get_url('/codes')
        data = {'phone': phone, 
                'code': code}
        return self.client.post(url, data=json.dumps(data))

