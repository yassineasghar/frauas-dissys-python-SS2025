from datetime import datetime

import zmq


class Server:
    ADDRESS: str = 'tcp://*:5555'
    TIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'
    ENCODING: str = 'utf-8'

    def __init__(self) -> None:
        self.context: zmq.Context | None = None
        self.socket: zmq.Socket | None = None
        self.initialize()

    def initialize(self) -> None:
        self.create_context()
        self.create_socket()
        self.bind_socket()

    def create_context(self) -> None:
        self.context = zmq.Context()

    def create_socket(self) -> None:
        self.socket = self.context.socket(socket_type=zmq.REP)

    def bind_socket(self) -> None:
        self.socket.bind(addr=self.ADDRESS)

    def receive_message(self) -> str:
        message = self.socket.recv_string()
        return message

    def send_message(self, message: str) -> None:
        self.socket.send_string(message)

    def run(self) -> None:
        print('Server started')
        while True:
            request = self.receive_message()
            print(request)

            now = datetime.now().strftime(self.TIME_FORMAT)
            reply_text = input(f'[{now}]> ')

            reply = f'[{now}][SERVER]: {reply_text}' if reply_text else ''
            self.send_message(reply)

    def close(self) -> None:
        if self.socket:
            self.socket.close()
        if self.context:
            self.context.term()


def main() -> None:
    server = Server()
    try:
        server.run()
    except KeyboardInterrupt:
        print('\nServer interrupted')
    finally:
        server.close()


if __name__ == '__main__':
    main()
