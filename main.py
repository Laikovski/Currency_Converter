import requests
import json
user_input = input().lower()
URL = f'http://www.floatrates.com/daily/{user_input}.json'

def request(url):
    r = requests.get(url.lower())
    if r.status_code == 200:
        res = json.loads(r.text)
        return res
    else:
        print("Something went wrong, try again")
request(URL)

def get_info():
    json_string = request(URL)
    print(json_string['usd'])
    print(json_string['eur'])
get_info()