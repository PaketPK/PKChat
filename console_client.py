import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except:
            break

def main():
    nickname = input("Enter your nickname: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("offers-visits.gl.at.ply.gg", 25025))
    client_socket.send(nickname.encode("utf-8"))

    recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    recv_thread.daemon = True
    recv_thread.start()

    try:
        while True:
            message = input()
            if message.lower() == "exit":
                client_socket.send(message.encode("utf-8"))
                break
            client_socket.send("{}: {}".format(nickname, message).encode("utf-8"))
    except KeyboardInterrupt:
        client_socket.close()

if __name__ == "__main__":
    main()
