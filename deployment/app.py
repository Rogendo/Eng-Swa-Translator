from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from translator import translate_text

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qwerty4578'

app = Flask(__name__, static_folder='static')
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(message):
    translated_text = translate_text(message)
    data = {
        'original': message,
        'translated': translated_text
    }
    emit('message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
