#!/usr/bin/env python
import os
import json
import requests
from beacons.portal.models import Header, IBeacon
from beacons.portal.helper import BeaconHelper, URLBuilder
from config import REGISTER_BEACONS, ERROR, SUCCESS, LIST_BEACONS, \
    USER_INFO, ESTIMOTE_CMD, NAMESPACE


beacon_helper = BeaconHelper()
url_builder = URLBuilder()


def list_beacons(credentials):
    """
    Returns list of the registered beacons
    """
    header = Header(credentials.access_token)
    response = requests.get(LIST_BEACONS, headers=header.get_header_body())
    return json.loads(response.content)


def list_beacons_attachment(beacon, credentials):
    """
    Returns list of all the attachments to the beacon
    """
    header = Header(credentials.access_token)
    url = url_builder.beacon_view_attachment_url(beacon)
    response = requests.get(url, headers=header.get_header_body())
    return response.content


def register_beacon(beacon, credentials):
    """
    Retun the response
    """
    request_body = beacon.registration_request_body()
    header = Header(credentials.access_token)
    response = requests.post(REGISTER_BEACONS, data=json.dumps(request_body),
        headers=header.get_header_body())
    return json.loads(response.content)


def deactivate_beacon(beacon_details, credentials):
    """
    Retun the response
    """
    header = Header(credentials.access_token)
    url = url_builder.beacon_deactivation_url(beacon_details)
    response = requests.post(url, headers=header.get_header_body())
    status = ERROR if response.status_code is 400 else SUCCESS
    return status


def activate_beacon(beacon_details, credentials):
    """
    Retun the response
    """
    header = Header(credentials.access_token)
    url = url_builder.beacon_activation_url(beacon_details)
    response = requests.post(url, headers=header.get_header_body())
    status = ERROR if response.status_code is 400 else SUCCESS
    return status


def attach_data_to_beacon(beacon_details, credentials):
    """
    Attaches data to beacon
    """
    request_body = beacon_details.attachment_request_body()
    header = Header(credentials.access_token)
    delete_url = url_builder.batch_delete_url(beacon_details)
    status = requests.post(delete_url, headers=header.get_header_body())
    url = url_builder.beacon_attachment_url(beacon_details)
    if status.status_code is 200:
        response = requests.post(url, data=json.dumps(request_body),
            headers=header.get_header_body())
    return response.content


def modify_beacon(beacon, credentials):
    """
    Modify the details of existing beacons
    """
    header = Header(credentials.access_token)
    request_body = beacon.update_request_body()
    url = url_builder.beacon_modification_url(beacon)
    response = requests.put(url, data=json.dumps(request_body),
        headers=header.get_header_body())
    return json.loads(response.content)


def get_session_username(credentials):
    """
    Returns the name of the user of the logged in User
    """
    header = Header(credentials.access_token)
    response = requests.get(USER_INFO, headers=header.get_header_body())
    return str(json.loads(response.content).get('name'))


def get_estimote_details(advertised_id):
    """
    Returns the namespace and instance id of the beacon
    """
    result = os.popen(ESTIMOTE_CMD).read()
    beacon_list = json.loads(result)
    for beacon in beacon_list:
        beacon_advertised_id = IBeacon(beacon).advertised_id()
        if advertised_id == beacon_advertised_id:
            return beacon
    return None


def namespace_of_beacon(credentials):
    """
    NameSpace of beacon
    """
    header = Header(credentials.access_token)
    response = requests.get(NAMESPACE, headers=header.__str__())
    return json.loads(response.content)


def get_beacon_details(credentials, beacon):
    """
    Returns the beacon instance
    """
    header = Header(credentials.access_token)
    url = url_builder.beacon_modification_url(beacon)
    response = requests.get(url, headers=header.get_header_body())
    return json.loads(response.content)
