import requests
import json
import pprint
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

def get_all_posts():
    resp = requests.get(url, headers=headers)
    results = json.loads(resp.text)
    for item in results:
        pprint.pprint(item)
    print('You have', len(results), 'posts', end='.\n')

def delete_post():
    id = input('type the id of the post you want to delete: ')
    delete_url = url + id + '/'
    resp = requests.delete(delete_url, headers=headers)
    print(resp.text)

def update_post():
    id = input('type the id of the post you want to update: ')
    update_url = url + id + '/'

    title = input('New title: ')
    content = input('New content: ')
    author = input('New author: ')
    data = {
        'title': title,
        'content': content,
        'author': author
    }
    resp = requests.put(update_url, headers=headers, data=json.dumps(data))
    print(resp.url)
    print(resp.text)



# Posts Tester
while True:
    print('''
        1 - get all posts
        2 - create random post
        3 - update post
        4 - delete post 
        5 - quit  
    ''')
    choice = input('What would you like to do (1-5)? ').strip()
    if choice == '1':
        get_all_posts()
    elif choice == '2':
        create_post()
    elif choice == '3':
        update_post()   
    elif choice == '4':
        delete_post()
    elif choice == '5':
        print('Quitting...')
        break
    else:
        print('Invalid choice. Please try again.')
    print()
    input('Press Enter to continue...')

