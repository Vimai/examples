import falcon
from api.resources.home import Home
from api.resources.users import Users


def create():
    api = falcon.API()
    api.add_route('/', Home())
    api.add_route('/users', Users())
    return api


app = application = create()
