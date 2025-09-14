import socket

HOST = "192.168.1.11"  
PORT = 8000        

def process_request(request):
    parts = request.strip().split()
    if not parts:
        return "Comando inválido"

    cmd = parts[0].lower()

    try:
        if cmd == "soma":
            nums = list(map(float, parts[1:]))
            return str(sum(nums))

        elif cmd == "sub":
            if len(parts) >= 3:
                return str(float(parts[1]) - float(parts[2]))
            else:
                return "Uso: sub x y"

        elif cmd == "mult":
            result = 1
            for n in map(float, parts[1:]):
                result *= n
            return str(result)

        elif cmd == "div":
            if len(parts) >= 3:
                y = float(parts[2])
                if y == 0:
                    return "Erro: divisão por zero"
                return str(float(parts[1]) / y)
            else:
                return "Uso: div x y"

        elif cmd == "invert":
            return parts[1][::-1] if len(parts) > 1 else "Uso: invert texto"

        elif cmd == "sort":
            nums = list(map(int, parts[1:]))
            return str(sorted(nums))

        elif cmd == "search":
            if len(parts) < 3:
                return "Uso: search valor lista"
            valor = int(parts[1])
            nums = list(map(int, parts[2:]))
            return "Encontrado" if valor in nums else "Não encontrado"

        else:
            return "Não reconhecido"

    except Exception as e:
        return f"Erro: {e}"

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Servidor rodando em {HOST}:{PORT}...")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conexão com {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    request = data.decode()
                    print(f"Recebido: {request}")
                    response = process_request(request)
                    conn.sendall(response.encode())

if __name__ == "__main__":
    main()
