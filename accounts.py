import requests
import json

import secrets
url = 'http://api.reimaginebanking.com'
key = '?key={}'.format(secrets.API_KEY)

def post_account(customer_id, account_info): 
	
    uri='/customers/{0}/accounts'.format(customer_id)
    print uri
    print account_info
    """
    account_info={
    "_id": "string",
    "type": "Credit Card",
    "nickname": "string",
    "rewards": 0,
    "balance": 0,
    "account_number": "string",
    "customer_id": "string"
  }
  """
    actual_url=url+uri+key
    response=requests.post(actual_url, json=account_info)
    print('account response')
    print response.json()
    account = response.json()['objectCreated']
    print('account')
    print account
    return account

def get_account_by_customer(customer_id=None):
    accounts = []
    uri = '/accounts'

    if customer_id is None:
        actual_url = url+uri+key
        reqeust = requests.get(actual_url)
        for a in request.json():
            accounts.append(a)

    else:
        id_uri = '/customers/{0}/accounts'.format(str(customer_id))
        actual_url = url+id_uri+key
        request = requests.get(actual_url)
        for a in request.json():
            accounts.append(a)

    return accounts

def get_account_by_id(account_id):

    uri = '/accounts/{}'.format(account_id)
    actual_url = url + uri + key
    request = requests.get(actual_url)

    return request.json()
