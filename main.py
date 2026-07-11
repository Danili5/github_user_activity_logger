from urllib.request import urlopen
import json
import sys

while True:
    try:
        print('input username or quit')
        username = input('>>> ')

        if username == 'quit':
            break

        with urlopen(f'https://api.github.com/users/{username}/events') as response:
            print(json.loads(response.read()))
    except:
        print('an expection has occurred.')