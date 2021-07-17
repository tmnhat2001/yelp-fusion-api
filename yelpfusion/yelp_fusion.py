from yelpfusion.endpoints.autocomplete import Autocomplete
from yelpfusion.endpoints.businesses import Businesses
from yelpfusion.endpoints.categories import Categories
from yelpfusion.endpoints.events import Events
from yelpfusion.endpoints.transactions import Transactions


class Api:
    def __init__(self, api_key: str):
        self.autocomplete = Autocomplete(api_key)
        self.businesses = Businesses(api_key)
        self.categories = Categories(api_key)
        self.events = Events(api_key)
        self.transactions = Transactions(api_key)
