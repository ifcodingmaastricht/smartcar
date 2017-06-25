import json
import socketio
import eventlet
import eventlet.wsgi
from flask import Flask, render_template
from Move import Car

car = Car()

sio = socketio.Server()
app = Flask(__name__)

@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.html')

@sio.on('connect', namespace='/chat')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('broadcast', namespace='/chat')
def message(sid, data):
    print(data)
    # car.move(25 * data["pitch"])
    #if data["roll"] > 2:
    #    car.turn(20)
    #elif data["roll"] < -2:
    #    car.turn(-20)
    #else:
    #    car.turn(0)
    # car.turn(25 * data["roll"])

    # if abs(data["pitch"]) > 1:
    #     car.move(data["pitch"]*10, data["pitch"]*10)
    # else:
    #     car.move(0,0)

    speed = pitch_to_move(data["pitch"], 4.0)
    turn = pitch_to_move(data["roll"], 2.0)
    car.move(speed, speed, turn)

@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
    print('disconnect ', sid)

def pitch_to_move(pitch, threshold):
    if abs(pitch) < threshold:
        return 0
    elif pitch > 0:
        return (pitch - threshold) * 100.0 / (10.0 - threshold)
    else:
        return (pitch + threshold) * 100.0 / (10.0 - threshold)


if __name__ == '__main__':
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
