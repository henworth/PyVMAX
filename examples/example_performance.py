#!/usr/bin/python

import sys
import os
import argparse
import datetime
import time
import logging

sys.path.insert(0, os.path.abspath('..'))
import pyvmax

#################################
### Define and Parse CLI arguments
PARSER = argparse.ArgumentParser(description='Example implementation of a Python REST client for EMC Unisphere for VMAX performance statistics.')
RFLAGS = PARSER.add_argument_group('Required arguments')
RFLAGS.add_argument('-url', required=True, help='Base Unisphere URL. e.g. https://10.0.0.1:8443')
RFLAGS.add_argument('-user', required=True, help='Unisphere username. e.g. smc')
RFLAGS.add_argument('-passwd', required=True, help='Unisphere password. e.g. smc')
ARGS = PARSER.parse_args()

URL = ARGS.url
USER = ARGS.user
PASSWORD = ARGS.passwd

log = logging.getLogger('example_performance.py')

vmax_api = pyvmax.connect(URL, USER, PASSWORD)

def time_now():
    return int(time.time() * 1000)

def time_minutes_ago(minutes=1):
    return int(time_now() - (minutes * 60 * 1000))

def time_hours_ago(hours=1):
    return int(time_now() - (hours * 3600 * 1000))

def time_days_ago(days=1):
    return int(time_now() - (days * 24 * 3600 * 1000))

def time_weeks_ago(weeks=1):
    return int(time_now() - (weeks * 7 * 24 * 3600 * 1000))

def time_last_midnight():
    today = datetime.date.today()
    return int(time.mktime(today.timetuple()) * 1000)

def time_midnights_ago(midnights=1):
    return int(time_last_midnight() - (midnights * 24 * 3600 * 1000))

def generate_payload(symmetrix_id):
    return {
        "startDate": time_minutes_ago(10),     # 60 minutes ago
        "endDate": time_now(),              # now
        "symmetrixId": symmetrix_id,
        "dataFormat": "Average",
        "metrics": ["IO_RATE", "PERCENT_HIT", "PERCENT_READ"]
    }


# Get all VMAXs for a given Unisphere Instance
symmetrix_list_response = vmax_api.get_arrays()
if 'symmetrixId' in symmetrix_list_response:
    symmetrix_list = symmetrix_list_response["symmetrixId"]
    log.info("VMAXs found: " + str(symmetrix_list))


# For each VMAX in Unisphere, get the array stats
for symm_id in symmetrix_list:
    perf_response = vmax_api.get_perf_array_metrics(generate_payload(symm_id))
    print(vmax_api.rest.json_to_str(perf_response))


