import urllib.request,json
from .models import Quotes

base_url = None

def configure_request(app):

    global base_url
    base_url = app.config['QUOTES_URL']

def get_quotes():

    quote_object = None

    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        if get_quote_response:
            
            author = get_quote_response.get('author')
            quote = get_quote_response.get('quote')
            quote_object = Quotes(author,quote)
    return quote_object