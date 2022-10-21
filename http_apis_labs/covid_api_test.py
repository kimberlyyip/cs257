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
    url = f'{API_BASE_URL}'
    #/v1/states/current.json