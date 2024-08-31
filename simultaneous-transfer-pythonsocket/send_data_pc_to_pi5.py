import socket

def start_server(host='192.168.1.20', port=12345):
    # Create a server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the specified host and port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"Server is listening on {host}:{port}...")
    
    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f"Connection accepted from: {addr}")
    
    # Receive a message
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Received message: {message}")
    
    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    start_server(host='192.168.1.20', port=12345)
