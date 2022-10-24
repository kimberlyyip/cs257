'''
covid_api_test.py

A program to retrieve results from an HTTP-based API, parse the results (JSON in this case), and manage the potential errors.
'''

import sys
import argparse
import json
import urllib.request

API_BASE_URL = 'https://api.covidtracking.com'

def get_state_cases(state):
    url = f'{API_BASE_URL}/v1/states/{state}/current.json'
    data_from_server = urllib.request.urlopen(url).read()
    string_from_server = data_from_server.decode('utf-8')
    state_case_list = json.load(string_from_server)
    result_list = []
    for case_dictionary in state_case_list:
        date = case_dictionary.get('date', '')
        positive_cases = case_dictionary.get('positive', '')
        deaths = case_dictionary.get('death', '')