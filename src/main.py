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

graphql = fetch_graphql(config, query)
rest = fetch_rest(config)

print(f'GraphQL response length: {len(graphql.content)}')

# Porque essa diferença discrepante de tamanho?
# O Graphql por ser uma query mais específica, retorna apenas os dados que foram solicitados.
# Já o Rest, retorna todos os dados do endpoint, o que pode ser muito mais do que o necessário.

print(f'Rest response length: {len(rest.content)}')