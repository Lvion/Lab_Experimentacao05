from dotenv import load_dotenv
from graphql_client import fetch_graphql
from rest_client import fetch_rest
import os

load_dotenv()

with open('misc/request.graphql', 'r') as query_file:
    query = query_file.read()

token = os.getenv('GITHUB_TOKEN')

config = {
    'url_graphql': 'https://api.github.com/graphql',
    'url_rest': 'https://api.github.com/search/repositories',
    'authorization': f'Bearer {token}'
}

top_repositories = fetch_graphql(config, query)
top_repositories2 = fetch_rest(config)

for edge in top_repositories:
    node = edge['node']
    print(f"Repository: {node['name']}, Owner: {node['owner']['login']}, Stars: {node['stargazerCount']}")

print("\n===========================================================================================\n")

for repo in top_repositories2:
    print(f"Repository: {repo['name']}, Owner: {repo['owner']['login']}, Stars: {repo['stargazers_count']}")