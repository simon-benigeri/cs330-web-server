import requests
import json
import random
import pprint
from faker import Faker
fake = Faker()

headers = { 'Content-Type': 'application/json' }
root_url = 'http://127.0.0.1:5000/'

def get_list_url(nested=False):
    if not nested:
        return root_url + 'api/comments/'
    url = root_url + 'api/posts/'
    resp = requests.get(url, headers=headers)
    data = json.loads(resp.text)
    # idx = random.randint(0, len(data) - 1)
    idx = 0
    comments_url = data[idx].get('comments_url')
    # print(comments_url)
    return comments_url

def create_comment():
    comments_url = get_list_url()
    data = {
        'comment': fake.sentence(),
        'author': fake.name()
    }
    resp = requests.post(comments_url, headers=headers, data=json.dumps(data))
    print(resp.url)
    print(resp.text)

def get_comments_by_post():
    comments_url = get_list_url()
    resp = requests.get(comments_url, headers=headers)
    results = json.loads(resp.text)
    for item in results:
        pprint.pprint(item)
    print('You have', len(results), 'comments', end='.\n')

def delete_comment():
    comments_url = get_list_url()
    id = input('type the id of the comment you want to delete: ')
    comments_url += id + '/'
    resp = requests.delete(comments_url, headers=headers)
    print(resp.text)

def update_comment():
    comments_url = get_list_url()
    id = input('type the id of the comment you want to update: ')
    comments_url += id + '/'

    comment = input('New comment: ')
    data = {
        'comment': comment
    }
    resp = requests.put(comments_url, headers=headers, data=json.dumps(data))
    print(resp.url)
    print(resp.text)



# Posts Tester
while True:
    print('''
        1 - get all comments (for a post)
        2 - create random comment
        3 - update comment
        4 - delete comment
        5 - quit  
    ''')
    choice = input('What would you like to do (1-5)? ').strip()
    if choice == '1':
        get_comments_by_post()
    elif choice == '2':
        create_comment()
    elif choice == '3':
        update_comment()   
    elif choice == '4':
        delete_comment()
    elif choice == '5':
        print('Quitting...')
        break
    else:
        print('Invalid choice. Please try again.')
    print()
    input('Press Enter to continue...')

