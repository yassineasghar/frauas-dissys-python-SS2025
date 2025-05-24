import socket
from datetime import datetime


class Server:
    _UTF_8 = 'utf-8'
    _BUFFER_SIZE = 1024
    _LOCAL_HOST = 'localhost'
    _TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    def __init__(self, host: str, port: int) -> None:
        self.host = host or self._LOCAL_HOST
        self.port = port
        self.socket = None
        self.__init_socket__()

    def __init_socket__(self) -> None:
        try:
            self._create_socket()
            self._bind_socket()
            self._listen_for_connections()
            self.connection, self.address = self._accept_connection()
        except OSError as err:
            print(f'ServerError: {str(err)}, Type: {type(err).__name__}')
            raise

    def run(self) -> None:
        while True:
            client_message = self.get_client_message(self.connection)
            if client_message:
                print(client_message)

            current_time = datetime.now().strftime(self._TIME_FORMAT)
            server_input = input(f"[{current_time}]> ")
            if server_input:
                self.send_message(self.connection, server_input)

    def get_client_message(self, connection) -> str:
        client_message = connection.recv(self._BUFFER_SIZE)
        return client_message.decode(self._UTF_8) if client_message else ''

    def send_message(self, connection, message: str) -> None:
        current_time = datetime.now().strftime(self._TIME_FORMAT)
        formatted_message = f'[{current_time}][SERVER]: {message}'
        connection.send(formatted_message.encode(self._UTF_8))

    def _create_socket(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _bind_socket(self) -> None:
        self.socket.bind((self.host, self.port))

    def _listen_for_connections(self) -> None:
        self.socket.listen()

    def _accept_connection(self) -> tuple:
        return self.socket.accept()


def main() -> None:
    server = Server(host='localhost', port=1337)
    server.run()


if __name__ == '__main__':
    main()
