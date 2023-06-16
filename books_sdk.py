import requests

class TokenError(Exception):
    pass

def check_token(token):
    params = {'token': token}
    endpoint = 'https://debug-server.voron434.repl.co/books/check_token'
    response = requests.get(endpoint, params=params)
    if response.status_code in [401, 403]:
        raise TokenError(response.text)
    response.raise_for_status()
    return response.ok


def get_book_by_id(token, book_id):
    params = {'token': token}
    endpoint = f'https://debug-server.voron434.repl.co/books/{book_id}'
    response = requests.get(endpoint, params=params)
    if response.status_code in [401, 403]:
        raise TokenError(response.text)
    response.raise_for_status()
    return response.json()


def get_author(book):
    return book['author']