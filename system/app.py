import socket
from router import router

class app:
    # Hostname
    server_host = "localhost"
    # Port
    server_port = 7200

    def __init__(self, host, port) -> None:
        if host is not None:
            self.server_host = host
        if port is not None:
            self.server_port = port

    def serve(self) -> None:
        # Creating a socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Setting socket
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Binding socket
        server_socket.bind((self.server_host, self.server_port))
        # Serve
        server_socket.listen(1)
        print('Server started on port %s ...' % self.server_port)

        while True:
            client_connection, client_address = server_socket.accept()

            request = client_connection.recv(1024).decode()
            print(router)
            
            # Initiate router
            rt = router()
            rt.boot()

            # html = self.get_init_content()

            # response = 'HTTP/1.0 200 OK\n\n' + html
            # client_connection.sendall(response.encode())
            # client_connection.close()
 
    def close(self, server_socket):
        server_socket.close()
