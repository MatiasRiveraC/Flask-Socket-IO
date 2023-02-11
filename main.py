from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["CORS_HEADER"] = "Content-Type"
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    print("TEST")
    socketio.emit('after connect', {'data':'Let us learn Web Socket in Flask'})

@socketio.on('message')
def test_connect2(data):
    print(data)
    socketio.emit('after connect', {'data':data})
    
@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)