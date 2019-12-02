import arcade
import socket
import server
import threading


class GameClient(arcade.Window):
    def __init__(self, addr):
        super().__init__(1000, 1000, "Cliet")
        self.message = ""
        self.server_addr = addr

    def on_update(self, delta_time: float):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"Got message from serve: {self.message}", 200, 200, color=(30, 40, 200), font_size=20)


def communicate_with_server(client: GameClient):
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    while True:
        network_message = str.encode("Client Says Hi")
        client_socket.sendto(network_message, (client.server_addr, server.SERVER_PORT))
        data_packet = client_socket.recvfrom(1024)
        data = data_packet[0]
        client.message = data

def main():
    server_addr = input("What is the server:")
    window = GameClient(server_addr)
    client_thread = threading.Thread(target=communicate_with_server,
                                     args=(window,), daemon=True)
    client_thread.start()
    arcade.run()

if __name__ == '__main__':
    main()

