import socketio
from assets import logger


class SocketClient:
    def __init__(self, url: str):
        self.url = url
        self.sio = socketio.Client()

        @self.sio.event
        def connect():
            logger.print_info("connection established")
            self.send_message('--client:connect-success', "Hello from Client.")

        @self.sio.on('--server:connect-success')
        def on_message(data):
            print('[RECEIVED]', data)

        @self.sio.event
        def disconnect():
            logger.print_error("disconnected from server")

    def send_message(self, evt, data):
        self.sio.emit(evt, data)

    def connect(self):
        self.sio.connect(self.url, transports=["websocket"])
