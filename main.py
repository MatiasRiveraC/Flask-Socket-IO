from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from setup import db
import models

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/ethicapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)
app.config["CORS_HEADER"] = "Content-Type"
socketio = SocketIO(app, cors_allowed_origins="*", engineio_logger=True, logger=True, async_mode='gevent', websocket_ping_interval=None)

@app.route('/')
def index():
    first_user = models.User.query.order_by(models.User.id.desc()).first()
    # Access properties of the first User
    print(first_user.name)

    return {}

@socketio.on('connect')
def test_connect():
    print("TEST")
    socketio.emit('after connect', {'data':'Let us learn Web Socket in Flask'})

@socketio.on('message')
def test_connect2(data):
    print(data)
    socketio.emit('Response', {'data':data})
    
@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)