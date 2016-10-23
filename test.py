
import requests
import json

from rapidconnect import RapidConnect
rapid = RapidConnect('hacktx-capitalone', '8c96cca2-e195-415b-b598-d16162d54b05');

import secrets

url = 'http://api.reimaginebanking.com'
key = '?key={}'.format(secrets.API_KEY)


def post_customer(info):
    uri = '/customers'

    """
    info = {
        "first_name": cust["string2",
        "last_name": "string2",
        "address": {
            "street_number": "string2",
            "street_name": "string",
            "city": "string",
            "state": "tx",
            "zip": "78705"
            }
        }
    """
    final_url = url + uri + key
    res = requests.post(final_url, json=info)
    account = res.json()['objectCreated']
    return account


def get_id(f_name, l_name):
    customers = get_customers()
    _id = None
    for c in customers:
        if c['first_name'] == f_name and c['last_name'] == l_name:
            _id = c['_id']
            return _id

    return None 


def get_customers(ids=None):
    customers = []
    uri = '/customers'

    if ids is None:
        final_url = url + uri + key
        res = requests.get(final_url)
        for a in res.json():
            print("id: {0}\n\tname: {1} {2}".format(a['_id'], a['first_name'], a['last_name']))
            customers.append(a)

        return customers

    for _id in ids:
        print _id
        id_uri = "{0}/{1}".format(uri, str(_id))
        final_url = url + id_uri + key
        res = requests.get(final_url)
        print 'res'
        print res.json()
        customers.append(res.json())

        return customers

def get_branches(ids=None):
    branches = []
    uri = '/branches'

    if ids is None:
        final_url = url + uri + key
        res = requests.get(final_url)
        for a in res.json():
            branches.append(a)

        return branches

    for _id in ids: 
        id_uri = "{0}/{1}".format(uri, str(_id))
        final_url = url + id_uri + key
        res = requests.get(final_url)

        for a in res.json():
            branches.append(res)

        return branches

def get_geo(address):
    result = rapid.call('GoogleGeocodingAPI', 'addressToCoordinates', {
        'apiKey': secrets.GOOGLE_KEY,
        'address': "{0} {1}, {2}, {3} {4}".format(
            address['street_number'], address['street_name'], address['city'], 
            address['state'], address['zip'])
        });
    print(result)

def get_address(latitude, longitude):
    result = rapid.call('GoogleGeocodingAPI', 'coordinatesToAddress', { 
        'apiKey': secrets.GOOGLE_KEY,
        'latitude': latitude,
        'longitude': longitude
    });
    print(result)







