from testapp import app
from testapp.blueprints import *


app.register_blueprint(TestIndex)
