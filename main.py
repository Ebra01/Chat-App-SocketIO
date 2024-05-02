from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET'] = 'SECRET!'
socketio = SocketIO(app, cors_allowed_origins='*')

@socketio.on('message')
def handle_message(msg):
    print('Received Message: ', msg)
    if msg != "User connected!":
        send(msg, broadcast=True)
        
@app.route('/')
def index():
    return render_template('index.html')
  
if __name__ == '__main__':
    socketio.run(app, debug=True)