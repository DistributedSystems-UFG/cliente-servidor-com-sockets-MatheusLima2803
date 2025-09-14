import socket

HOST = "192.168.1.11"  
PORT = 8000

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("Conectado ao servidor. Digite comandos (ex: soma 3 4, invert casa, sort 5 2 9).")
        print("Digite 'exit' para sair.")
        
        while True:
            msg = input(">> ")
            if msg.lower() == "exit":
                break
            s.sendall(msg.encode())
            data = s.recv(1024)
            print("Resposta:", data.decode())

if __name__ == "__main__":
    main()
