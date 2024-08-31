import socket

def send_message(host='192.168.1.20', port=12345, message='Hello, PC!'):
    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Send a message
    client_socket.send(message.encode('utf-8'))
    print("Message sent.")
    
    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    send_message(host='192.168.1.20', port=12345)
