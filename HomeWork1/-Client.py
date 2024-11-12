import socket

# Connect to the server and start the chat
def start_client():
    # Create a socket object for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define server's IP address and port to connect to
    server_ip = '127.0.0.1'  # Assuming the server is on the same machine (localhost)
    server_port = 12345       # Port used by the server
    
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    print(f"Connected to server {server_ip}:{server_port}")
    
    # Start the chat session with the server
    while True:
        # Send message to server
        client_message = input("Client: ")
        client_socket.send(client_message.encode())
        
        # If the client sends 'exit', break the chat session
        if client_message.lower() == 'exit':
            print("Client disconnected.")
            break
        
        # Receive the response from the server
        server_message = client_socket.recv(1024).decode()
        print(f"Server: {server_message}")
        if server_message.lower() == 'exit':
            print("Server disconnected.")
            break

    # Close the socket after the chat ends
    client_socket.close()

# Start the client
if __name__ == "__main__":
    start_client()
