import requests

headers = { 'Content-Type': 'application/json' }
url = 'http://127.0.0.1:5000/api/posts/'


# See documentation: https://developers.google.com/youtube/v3/docs/search/list
def get_youtube_videos(search_term='cute puppies'):
    url = 'https://www.apitutor.org/youtube/simple/'
    params = {
        'q': search_term
    }
    resp = requests.get(url, headers=headers, params=params)
    print(resp.url)
    print(resp.text)

# See documentation: https://developer.spotify.com/documentation/web-api/reference/#category-search
def get_spotify_tracks(search_term='Beyonce', resource_type='track'):
    url = 'https://www.apitutor.org/spotify/simple/v1/search'
    params = {
        'q': search_term,
        'type': resource_type
    }
    resp = requests.get(url, headers=headers, params=params)
    print(resp.url)
    print(resp.text)

# See documentation: https://www.yelp.com/developers/documentation/v3/business_search
def get_yelp_restaurants(location='Evanston, IL', search_term='pizza'):
    url = 'https://www.apitutor.org/yelp/simple/v3/businesses/search'
    params = {
        'location': location,
        'term': search_term
    }
    resp = requests.get(url, headers=headers, params=params)
    print(resp.url)
    print(resp.text)



# get_youtube_videos(search_term='cute puppies')
get_spotify_tracks(search_term='Beyonce')
get_yelp_restaurants(search_term='vietnamese')