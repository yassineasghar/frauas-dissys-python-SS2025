import zmq


class Subscriber:
    ADDRESS: str = 'tcp://localhost:5555'
    TOPIC: str = 'XYchat'
    ENCODING: str = 'utf-8'

    def __init__(self) -> None:
        self.context: zmq.Context | None = None
        self.socket: zmq.Socket | None = None
        self.initialize()

    def initialize(self) -> None:
        self.create_context()
        self.create_socket()
        self.set_topic_filter()
        self.connect_socket()

    def create_context(self) -> None:
        self.context = zmq.Context()

    def create_socket(self) -> None:
        self.socket = self.context.socket(socket_type=zmq.SUB)

    def set_topic_filter(self) -> None:
        self.socket.setsockopt_string(option=zmq.SUBSCRIBE, optval=self.TOPIC)

    def connect_socket(self) -> None:
        self.socket.connect(addr=self.ADDRESS)

    def listen(self) -> None:
        print('Subscriber started and listening')
        while True:
            raw_message = self.socket.recv_string()
            _, message = raw_message.split(sep=' ', maxsplit=1)
            print(message)

    def close(self) -> None:
        if self.socket:
            self.socket.close()
        if self.context:
            self.context.term()


def main() -> None:
    subscriber = Subscriber()
    try:
        subscriber.listen()
    except KeyboardInterrupt:
        print('\nSubscriber interrupted.')
    finally:
        subscriber.close()


if __name__ == '__main__':
    main()
