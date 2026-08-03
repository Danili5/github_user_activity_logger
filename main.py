import sys
import json
from urllib.request import urlopen

class Main:
    def search(self):
        try:
            self.username = sys.argv[1]
        except IndexError:
            self.username = input('enter the username: ')

        try:
            with urlopen(f'https://api.github.com/users/{self.username}/events') as response:
                for entry in json.loads(response.read()):
                    user = entry['actor']['login']
                    event = entry['type'].split('Event')[0].lower()
                    repository = entry['repo']['name']

                    print(f'> {user} has a {event} event to {repository}')
        except Exception as exception:
            print(exception)

main = Main()

while True:
    main.search()