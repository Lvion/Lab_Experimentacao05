import requests

def fetch_rest(_config):
    url = _config['url_rest']
    headers = {
        'Authorization': _config['authorization']
    }
    params = {
        'q': 'stars:>1',
        'sort': 'stars',
        'order': 'desc',
        'per_page': 10
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Query failed to run by returning code of {response.status_code}. {response.text}")
        return []