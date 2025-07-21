import zmq
from datetime import datetime


class Server:
    PUBLISHER_ADDRESS = 'tcp://*:5556'
    ROUTER_ADDRESS = 'tcp://*:5557'
    ENCODING = 'utf-8'
    TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self) -> None:
        self.context = zmq.Context()
        self.router = self.create_router_socket()
        self.publisher = self.create_publisher_socket()
        self.subscriptions = {}

    def create_router_socket(self):
        socket = self.context.socket(zmq.ROUTER)
        socket.bind(self.ROUTER_ADDRESS)
        return socket

    def create_publisher_socket(self):
        socket = self.context.socket(zmq.PUB)
        socket.bind(self.PUBLISHER_ADDRESS)
        return socket

    def log(self, msg: str) -> None:
        now = datetime.now().strftime(self.TIME_FORMAT)
        print(f'[{now}] {msg}')

    def receive_client_message(self) -> tuple[str, str, str]:
        identity, _, message = self.router.recv_multipart()
        client_id = identity.decode(self.ENCODING)
        channel, content = message.decode(self.ENCODING).split(' ', 1)
        return client_id, channel, content

    def add_subscription(self, client_id: str, channel: str) -> None:
        self.subscriptions.setdefault(channel, set()).add(client_id)
        self.log(f'Client {client_id} subscribed to "{channel}"')

    def publish_to_channel(self, client_id: str, channel: str, content: str) -> None:
        self.log(f'Message from {client_id} to "{channel}": {content}')
        self.publisher.send_string(f'{channel} {content}')
        receivers = self.subscriptions.get(channel, set())
        self.log(f'Forwarded to: {receivers}')

    def run(self) -> None:
        self.log('Server started.')
        try:
            while True:
                client_id, channel, content = self.receive_client_message()
                self.add_subscription(client_id, channel)
                self.publish_to_channel(client_id, channel, content)
        except KeyboardInterrupt:
            self.log('Server interrupted.')
        finally:
            self.router.close()
            self.publisher.close()
            self.context.term()


def main():
    Server().run()


if __name__ == '__main__':
    main()
