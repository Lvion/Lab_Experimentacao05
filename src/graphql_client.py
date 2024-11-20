import requests

def fetch_graphql(_config, _query):
    url = _config['url_graphql']
    headers = {
        'Authorization': _config['authorization']
    }

    response = requests.post(url, json={'query': _query}, headers=headers)

    if response.status_code == 200:
        return response
    else:
        print(f"Query failed to run by returning code of {response.status_code}. {response.text}")
        return fetch_graphql(_config, _query)