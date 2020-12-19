from flask import Flask, session, redirect, url_for, render_template, request
from functools  import wraps, update_wrapper
from flask_socketio import SocketIO


socketio = SocketIO()

app = Flask(__name__)



from testapp import views   ### Add the views seperately (incase you need to maintain this file seperately)
socketio.init_app(app)