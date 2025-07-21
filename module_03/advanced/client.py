import threading
from datetime import datetime
import zmq
import uuid


class Client:
    PUBLISHER_ADDRESS = 'tcp://localhost:5556'
    ROUTER_ADDRESS = 'tcp://localhost:5557'
    ENCODING = 'utf-8'
    TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, channel: str) -> None:
        self.channel = channel
        self.client_id = str(uuid.uuid4())[:8]
        self.context = None
        self.dealer_socket = None
        self.subscriber_socket = None
        self.initialize()

    def initialize(self) -> None:
        self.create_context()
        self.create_dealer_socket()
        self.create_subscriber_socket()
        self.connect_dealer_socket()
        self.connect_subscriber_socket()
        self.set_channel_filter()

    def create_context(self) -> None:
        self.context = zmq.Context()

    def create_dealer_socket(self) -> None:
        self.dealer_socket = self.context.socket(zmq.DEALER)
        self.dealer_socket.setsockopt_string(zmq.IDENTITY, self.client_id)

    def create_subscriber_socket(self) -> None:
        self.subscriber_socket = self.context.socket(zmq.SUB)

    def connect_dealer_socket(self) -> None:
        self.dealer_socket.connect(self.ROUTER_ADDRESS)

    def connect_subscriber_socket(self) -> None:
        self.subscriber_socket.connect(self.PUBLISHER_ADDRESS)

    def set_channel_filter(self) -> None:
        self.subscriber_socket.setsockopt_string(zmq.SUBSCRIBE, self.channel)

    def send_messages(self) -> None:
        print(f'Your ID is: {self.client_id}')
        print('You can now send messages:')
        while True:
            now = datetime.now().strftime(self.TIME_FORMAT)
            message = input('> ').strip()
            if message:
                formatted = f'{self.channel} [{now}][{self.client_id}] {message}'
                self.dealer_socket.send_multipart([b'', formatted.encode(self.ENCODING)])

    def receive_messages(self) -> None:
        while True:
            raw_message = self.subscriber_socket.recv_string()
            _, content = raw_message.split(' ', 1)
            print(f'\n[Received] {content}')

    def run(self) -> None:
        receiver = threading.Thread(target=self.receive_messages, daemon=True)
        receiver.start()
        try:
            self.send_messages()
        except KeyboardInterrupt:
            print('\nClient interrupted.')
        finally:
            self.close()

    def close(self) -> None:
        self.dealer_socket.close()
        self.subscriber_socket.close()
        self.context.term()


def main() -> None:
    channel = input('Enter channel to subscribe to: ').strip()
    client = Client(channel)
    client.run()


if __name__ == '__main__':
    main()
