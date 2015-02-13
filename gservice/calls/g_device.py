#coding:utf-8

'''
module::device
~~~~~~~~~~~~~~
Device operations
'''


from requests import Request
from g_common import API_URL, render_url
import logging

logging.basicConfig(level=logging.DEBUG)

def retrieve_device_histroy_data(did, start_ts=1349032093, end_ts=1349032093, entity=1, attr="temp", limit=20, skip=0):
    request_body = {'start_ts': start_ts,
                    'end_ts': end_ts,
                    'entity': entity,
                    'attr': attr,
                    'limit': limit,
                    'skip': skip
                    }
    url = render_url('/devdata/' + str(did))
    return Request("GET", url, params=request_body)

def retrieve_product_histroy_data(product_key, did=None, start_ts=1349032093, end_ts=1349032093, entity=1, attr="temp", limit=20, skip=0):
    request_body = {
        'product_key': product_key,
        'did':did,
        'start_ts': start_ts,
        'end_ts': end_ts,
        'entity': entity,
        'attr': attr,
        'limit': limit,
        'skip': skip
        }
    url = render_url('/devdata')
    return Request("GET", url, params=request_body)

#===bound device
def get_bound_devices(limit=20, skip=0):
    request_body = {
        'limit': limit,
        'skip': skip
        }
    return Request("GET", render_url('/bindings'), params=request_body)


def bind_devices(devices):
    '''
    :param devices: struct = > [('did', 'passcode', 'remark(optional)', ...]
    '''
    data_devices = []
    for d in devices:
        device = {'did': None, 'passcode': None}
        device['did'] = d[0]
        device['passcode'] = d[1]
        try:
            device['remark'] = d[2]
        except IndexError:
            pass
        data_devices.append(device)
    request_body = {'devices':data_devices}
    return Request("POST", render_url('/bindings'), data=request_body)
    

def unbind_devices(devices):
    data_devices = []
    for did, passcode in devices:
        device = {'did': None, 'passcode': None}
        device['did'] = did
        device['passcode'] = passcode
        data_devices.append(device)
    request_body = {'devices':data_devices}
    return Request("DELETE", render_url('/bindings'), data=request_body)

#===device detail
def device_detail(did):
    url = render_url('/devices/' + str(did))
    return Request("GET", url)

def query_device(product_key, mac):
    request_body = {
        'product_key': product_key,
        'mac':mac
        }
    return Request("GET", render_url('/devices'), params=request_body)

def remote_control_device(did, raw):
    '''
    :param did: did
    :type did: String

    :param raw: struct => [<byte>, <byte>, ...]
    :type raw: list
    '''
    request_body = {
        'raw': raw
        }
    url = render_url('/control/' + str(did))
    return Request("POST", url, data=request_body)

def create_scheduler(date, time, repeat, retry_count, retry_task, tasks):
    '''
    :param date: required if repeat is 'none'
    :param time: '2014-11-11'
    :param repeat: "none" or "mon", "tue", "wed", "thu", "fri", "sat", "sun"
    :param retry_count: retry totals
    :param retry_task: "all" or "failed"
    :param tasks: 
        struct => {
        "did": "did1",
        "product_key": "xxx",
            "attrs": {
            "attr1": val,
            "attr2": val
            }
        }
    '''
    request_body = {
        "time": time,
        "repeat": repeat,
        "task": tasks,
        "retry_count": retry_count,
        "retry_task": retry_task
        }
    if date:
        request_body['date'] = date
    url = render_url('/scheduler')
    logging.debug(url)
    logging.debug(request_body)
    return Request("POST", url, data=request_body)

def fetch_scheduler(skip=None, limit=None):
    '''
    :param limit: (optional)
    :param skip: (optional)
    '''
    request_body = {'limit':limit, 'skip':skip}
    url = render_url('/scheduler')
    return Request("GET", url, params=request_body)
    
def del_scheduler(sid):
    '''
    :param sid: scheduler id
    '''
    url = render_url('/scheduler/{0}'.format(sid))
    return Request("DELETE", url)

def scheduler_logs(sid):
    '''
    :param sid: scheduler id
    '''
    url = render_url('/scheduler/{0}/logs'.format(sid))
    return Request("GET", url)
