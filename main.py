import sys
import json
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

class Main:
    def search(self):
        try:
            self.username = sys.argv[1]
        except IndexError:
            self.username = input('enter username: ')

        try:
            with urlopen(f'https://api.github.com/users/{self.username}/events') as response:
                for event in json.loads(response.read()):
                    print(event['type'])
        except Exception as exception:
            print(exception)

main = Main()

while True:
    main.search()