'''
covid_api_test.py

A program to retrieve results from an HTTP-based API, parse the results (JSON in this case), and manage the potential errors.
'''

#Currently getting the error Jeff got in his sample program. Tried to implement his solution but it is still not working.

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
        result_list.append({'date':date, 'positive':positive_cases, 'death':deaths})
    return result_list

def main(args):
    if args.action == 'state':
        data = get_state_cases(args.state)
        for item in data:
            date = item['date']
            positives = item['positives']
            print(f'{date}[{positives}]')
    else:
        print('you did something wrong!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get case info from the COVID data API')
    parser.add_argument('action', metavar='action', help='action to perform on the word ("state")', choices=['state'])
    
    parser.add_argument('state', metavar='state',help='the state as a 2-character code', choices=['mn', 'hi', 'ny', 'ca'])

    args = parser.parse_args()
    main(args)