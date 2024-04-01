from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# List untuk menyimpan pesan
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@socketio.on('send_message')
def handle_message(data):
    username = data['username']
    message = data['message']
    messages.append({'username': username, 'message': message})
    emit('new_message', {'username': username, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
