import time
from datetime import datetime

import zmq


class Publisher:
    ADDRESS: str = 'tcp://*:5555'
    TOPIC: str = 'chat'
    TIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'
    ENCODING: str = 'utf-8'

    def __init__(self) -> None:
        self.context: zmq.Context | None = None
        self.socket: zmq.Socket | None = None
        self.create_context()
        self.create_socket()
        self.bind_socket()

    def create_context(self) -> None:
        self.context = zmq.Context()

    def create_socket(self) -> None:
        self.socket = self.context.socket(socket_type=zmq.PUB)

    def bind_socket(self) -> None:
        self.socket.bind(addr=self.ADDRESS)

    def publish(self, message: str) -> None:
        full_message = f'{self.TOPIC} {message}'
        self.socket.send_string(full_message)

    def run(self) -> None:
        print('Publisher started')
        while True:
            now = datetime.now().strftime(format=self.TIME_FORMAT)
            msg = input(f'[{now}]> ')
            if msg:
                self.publish(message=f'[{now}][SERVER]: {msg}')
                time.sleep(0.1)

    def close(self) -> None:
        self.socket.close()
        self.context.term()


def main() -> None:
    publisher = Publisher()
    try:
        publisher.run()
    except KeyboardInterrupt:
        print('\nPublisher interrupted.')
    finally:
        publisher.close()


if __name__ == '__main__':
    main()
