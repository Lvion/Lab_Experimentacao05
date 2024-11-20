import requests
import time

def fetch_graphql(_config, _query, max_retries=4, initial_delay=1):
    url = _config['url_graphql']
    retries = 0
    delay = initial_delay

    headers = {
        'Authorization': _config['authorization']
    }

    while retries < max_retries:
        response = requests.post(url, json={'query': _query}, headers=headers)
        if response.status_code == 200:
            return response
        elif response.status_code == 429:
            print(f"Rate limit exceeded. Retrying in {delay} seconds.")
            time.sleep(delay)
            delay *= 2
            retries += 1
        elif response.status_code in [502, 503]:
            print(f"Server error ({response.status_code}). Retrying in {delay} seconds.")
            time.sleep(delay)
            delay *= 2
            retries += 1
        else:
            print(f"Request failed with status code: {response.status_code} \n {response.json()}")
            break