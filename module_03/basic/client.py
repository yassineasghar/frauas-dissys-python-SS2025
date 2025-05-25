from datetime import datetime

import zmq


class Client:
    ADDRESS: str = 'tcp://localhost:5555'
    TIME_FORMAT: str = '%Y-%m-%d %H:%M:%S'
    ENCODING: str = 'utf-8'

    def __init__(self) -> None:
        self.context: zmq.Context | None = None
        self.socket: zmq.Socket | None = None

    def create_context_and_socket(self) -> None:
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)

    def connect_socket(self) -> None:
        self.socket.connect(self.ADDRESS)

    def send_message(self, message: str) -> None:
        self.socket.send_string(message)

    def receive_message(self) -> str:
        message = self.socket.recv_string()
        return message

    def run(self) -> None:
        self.create_context_and_socket()
        self.connect_socket()

        while True:
            now = datetime.now().strftime(self.TIME_FORMAT)
            text = input(f'[{now}]> ')
            if not text:
                continue

            message = f'[{now}][CLIENT]: {text}'
            self.send_message(message)

            reply = self.receive_message()
            print(reply)

    def close(self) -> None:
        if self.socket:
            self.socket.close()
        if self.context:
            self.context.term()


def main() -> None:
    client = Client()
    try:
        client.run()
    except KeyboardInterrupt:
        print('\nClient interrupted.')
    finally:
        client.close()


if __name__ == '__main__':
    main()
