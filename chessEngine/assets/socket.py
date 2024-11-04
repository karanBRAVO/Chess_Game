import socketio
from assets import logger


class SocketClient:
    def __init__(self, url: str):
        self.url = url
        self.sio = socketio.Client()

        @self.sio.event
        def connect():
            logger.print_info("connection established")

        @self.sio.event
        def disconnect():
            logger.print_error("disconnected from server")

    def send_message(self, evt, data):
        self.sio.emit(evt, data)

    def connect(self, user_details):
        self.sio.connect(self.url, transports=["websocket"], auth=user_details)

    def disconnect(self):
        self.sio.disconnect()
