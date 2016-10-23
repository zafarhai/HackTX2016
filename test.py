
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
    return res.json()


def get_id(f_name, l_name):
    customers = get_customers()
    id = None
    for c in customers:
        if c['first_name'] == f_name and c['last_name'] == l_name:
            id = c['_id']

    return id


def get_customers(ids=None):
    customers = []
    uri = '/customers'

    if ids is None:
        final_url = url + uri + key
        res = requests.get(final_url)
        for a in res.json():
            print("id: {0}\n\tname: {1} {2}".format(a['_id'], a['first_name'], a['last_name']))
            customers.add(a)

        return customers

    for id in ids:
        id_uri = "{0}/{1}".format(uri, str(id))
        final_url = url + id_uri + key
        res = requests.get(final_url)
        for a in res.json():
            customers.add(a)

        return customers

def get_branches(ids=None):
    branches = []
    uri = '/branches'

    if ids is None:
        final_url = url + uri + key
        res = requests.get(final_url)
        for a in res.json():
            branches.add(a)

        return branches

    for id in ids: 
        id_uri = "{0}/{1}".format(uri, str(id))
        final_url = url + id_uri + key
        res = requests.get(final_url)

        for a in res.json():
            branches.add(res)

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

def get_branches_near_loc(latitude, longitude):
    pass


address = {
    "street_number": "2624",
    "street_name": "Whitis Ave",
    "city": "Austin",
    "state": "TX",
    "zip": "78705"
    }

get_branch_geo(address)






