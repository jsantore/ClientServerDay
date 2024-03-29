import socket

SERVER_PORT = 20001

def find_server_address():
    server_address= ""
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        conn.connect(('10.255.255.255', 1))
        server_address = conn.getsockname()[0]
    except IOError:
        server_address = '127.0.0.1'
    finally:
        conn.close()
    return server_address

def run_server():
    server_address = find_server_address()
    player_pos = [500, 600]
    print(f"Server Listening on {server_address}  Port: {SERVER_PORT}")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_address, SERVER_PORT))
    while True:
        data_packet = server_socket.recvfrom(1024)
        data = data_packet[0]
        data = str(data, "UTF-8")
        if data.find("LEFT")>=0:
            player_pos[0] -=1
        elif data.find("RIGHT")>=0:
            player_pos[0]+= 1
        client_address = data_packet[1]
        encoded_message = str.encode(f"{player_pos[0]},{player_pos[1]}")
        server_socket.sendto(encoded_message, client_address)

if __name__ == '__main__':
    run_server()