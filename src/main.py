import time
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

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

graphql, graphql_time = measure_execution_time(fetch_graphql, config, query)
rest, rest_time = measure_execution_time(fetch_rest, config)

print(f'GraphQL response Length: {len(graphql.content)}, Execution time: {graphql_time:.4f} seconds')
print(f'Rest response Length: {len(rest.content)}, Execution time: {rest_time:.4f} seconds')