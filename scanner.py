import socket
import threading

open_ports = []  # Lista para guardar los puertos abiertos

def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # timeout más corto
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except:
        pass

def scan_ports_range(target_ip, start_port, end_port):
    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Mostrar resultados ordenados
    if open_ports:
        print(f"Puertos abiertos en {target_ip}: {sorted(open_ports)}")
    else:
        print(f"No se encontraron puertos abiertos en {target_ip}")

# Ejemplo de prueba
target = "escribir aqui tu ip"
scan_ports_range(target, 75, 85)
