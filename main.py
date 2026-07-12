import sys
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

try:
    user_input = sys.argv[1]
    with urlopen(f'https://api.github.com/users/{user_input}/events') as response:
        pushes = []
        username = ''

        for entry in json.loads(response.read()):
            if entry['type'] == 'PushEvent':
                pushes.append(entry)

        print(f'{user_input} has {len(pushes)} pushes')
except IndexError:
    print('ERROR: enter a username next to the filename of the program when running it.')
except HTTPError as exception:
    print(exception)
except URLError as exception:
    print(exception)