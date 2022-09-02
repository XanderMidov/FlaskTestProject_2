from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep import Client
from zeep.transports import Transport
from datetime import datetime

def get_1S_leftovers(date):
    session = Session()
    session.auth = HTTPBasicAuth('Python', '411209')
    client = Client('http://localhost/Chezima32/ru_RU/ws/chezima_items.1cws?wsdl',
        transport=Transport(session=session))

    results = client.service.GetItem(date)
    return results

