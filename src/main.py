import time
import pandas as pd
from dotenv import load_dotenv
from graphql_client import fetch_graphql
from rest_client import fetch_rest
import os

load_dotenv()

with open('misc/request.graphql', 'r') as query_file:
    query = query_file.read()

token = os.getenv('GITHUB_TOKEN')
EXECUTION_TIMES = 10

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

graphql_times = []
graphql_lengths = []
rest_times = []
rest_lengths = []

for _ in range(EXECUTION_TIMES):
    graphql, graphql_time = measure_execution_time(fetch_graphql, config, query)
    if graphql:
        graphql_times.append(graphql_time)
        graphql_lengths.append(len(graphql.content))

    rest, rest_time = measure_execution_time(fetch_rest, config)
    if rest:
        rest_times.append(rest_time)
        rest_lengths.append(len(rest.content))

data = {
    'graphql_times': graphql_times,
    'graphql_lengths': graphql_lengths,
    'rest_times': rest_times,
    'rest_lengths': rest_lengths
}
df = pd.DataFrame(data)
df.to_csv('execution_times.csv', index=False)