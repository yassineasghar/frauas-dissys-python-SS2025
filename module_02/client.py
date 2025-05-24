from datetime import datetime
from socket import socket, AF_INET, SOCK_STREAM


class Client:
    _UTF_8 = 'utf-8'
    _BUFFER_SIZE = 1024
    _LOCAL_HOST = 'localhost'
    _TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, host: str, port: int) -> None:
        self.host = host or self._LOCAL_HOST
        self.port = port
        self.socket = None

    def __init_socket__(self) -> None:
        try:
            self._create_socket()
            self._connect_socket()
        except OSError as err:
            print(f'ClientError: {str(err)}, Type: {type(err).__name__}')
            raise

    def run(self) -> None:
        try:
            self._create_socket()
            self._connect_socket()

            while True:
                current_time = datetime.now().strftime(self._TIME_FORMAT)
                client_input = input(f"[{current_time}]> ")
                if client_input:
                    self.send_message(f"[{current_time}][CLIENT]: {client_input}")

                server_response = self.socket.recv(self._BUFFER_SIZE)
                if server_response:
                    print(server_response.decode(self._UTF_8))

        except Exception as err:
            print(f'Error in Client: {str(err)}')
        finally:
            if self.socket:
                self.socket.close()

    def _create_socket(self) -> None:
        self.socket = socket(AF_INET, SOCK_STREAM)

    def _connect_socket(self) -> None:
        self.socket.connect((self.host, self.port))

    def send_message(self, message: str) -> None:
        self.socket.send(message.encode(self._UTF_8))


def main() -> None:
    client = Client(host='localhost', port=1337)
    client.run()


if __name__ == '__main__':
    main()
