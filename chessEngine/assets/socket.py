import socketio
from assets import logger
import time


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
        while not self.sio.connected:
            try:
                self.sio.connect(self.url, transports=[
                    "websocket"], auth=user_details)
            except socketio.exceptions.ConnectionError as e:
                logger.print_error(
                    f"Initial connection failed: {e}. Retrying...")
                time.sleep(5)

    def disconnect(self):
        self.sio.disconnect()
