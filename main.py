import sys
import json
from urllib.request import urlopen

class Main:
    def __init__(self):
        self.events = {}

    def search(self):
        try:
            self.username = sys.argv[1]
        except IndexError:
            self.username = input('enter the username: ')

        try:
            with urlopen(f'https://api.github.com/users/{self.username}/events') as response:
                for entry in json.loads(response.read()):
                    pass
        except Exception as exception:
            print(exception)

if __name__ == '__main__':
    main = Main()

    while True:
        main.search()