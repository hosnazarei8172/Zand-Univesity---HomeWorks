import socket

# Setting up the server to listen for incoming connections
def start_server():
    # Create a socket object for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define host and port for the server
    host = '0.0.0.0'  # Bind to all available network interfaces
    port = 12345       # Port to listen on
    
    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Start listening for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    # Accept incoming connection from client
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    # Start a chat session with the client
    while True:
        # Receive message from client
        client_message = client_socket.recv(1024).decode()
        if client_message.lower() == 'exit':
            print("Client disconnected.")
            break
        print(f"Client: {client_message}")
        
        # Send response back to client
        server_message = input("Server: ")
        client_socket.send(server_message.encode())
        if server_message.lower() == 'exit':
            print("Server disconnected.")
            break

    # Close the socket after chat ends
    client_socket.close()
    server_socket.close()

# Start the server
if __name__ == "__main__":
    start_server()
