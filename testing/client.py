import requests
import json
from faker import Faker
fake = Faker()

headers = { 'Content-Type': 'application/json' }
url = 'http://127.0.0.1:5000/api/posts/'

def create_post():
    data = {
        'title': fake.sentence(),
        'content': fake.text(),
        'author': fake.name()
    }
    resp = requests.post(url, headers=headers, data=json.dumps(data))
    print(resp.url)
    print(resp.text)

def get_posts():
    resp = requests.get(url, headers=headers)
    print(resp.text)


# Uncomment to test:
create_post()
get_posts()