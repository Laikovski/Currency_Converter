import requests
import json
import ast

user_input = input().lower() # sent

URL = f'http://www.floatrates.com/daily/{user_input}.json'

def request(url):
    r = requests.get(url.lower())
    if r.status_code == 200:
        res = json.loads(r.text)
        return res
    else:
        print("Something went wrong, try again")
request(URL)

def default_courses(user_input):
    arr = request(URL)
    currency = {}
    if user_input == 'usd':
        currency['eur'] = arr['eur']['rate']
    elif user_input == 'eur':
        currency['usd'] = arr['usd']['rate']
    else:
        currency['usd'] = arr['usd']['rate']
        currency['eur'] = arr['eur']['rate']
    while True:
        recive_money = input().lower()  # recive
        if recive_money == '':
            break
        else:
            count_money = ast.literal_eval(input())
            print('Checking the cache...')
            if recive_money in currency:
                print('Oh! It is in the cache!')
                print(f'You received {round(count_money * currency[recive_money], 2)} {recive_money.upper()}')
            else:
                print('Sorry, but it is not in the cache!')
                currency[recive_money] = arr[recive_money]['rate']
                print(f'You received {round(count_money * currency[recive_money], 2)} {recive_money.upper()}')

default_courses(user_input)