import socket # importa la libreria estandar de python para trabajar sockets
import threading

open_ports = []  # lista global para almacenar los puertos abiertoss

# Crear un  socket tcp IPv4
def scan_port(target_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #indica que usaremos direcciones IPv4 y que el socket sera tcp(flujo confiable)
        sock.settimeout(0.5) #tiempo de espera en respuesta
        result = sock.connect_ex((target_ip,port)) # Intenta conectarse al puerto 
        if result == 0: # si devuelve 0 esta abierto, sino es error o cerrado
            open_ports.append(port) # guarda el puerto abierto en la lista
        sock.close() # cierra el socket
    except:
        pass


# Permite que cienttos de puertos se escaneen al mismo tiempo
def scan_ports_range(target_ip, start_port, end_port):
    threads = []
    for port in range(start_port, end_port +1):
        thread = threading.Thread(target=scan_port, args=(target_ip, port)) # Crea un hilo que ejecuta  la funcion scan_port y  pasa los parametros necesarios al hilo
        threads.append(thread) # Cada puerto se escanea en un hilo independiente
        thread.start() # Inicia el hilo

    for thread in threads:
        thread.join()  # Espera que el hilo termine antes de continuar

    if open_ports:
        print(f"Puertos abiertos en {target_ip}: {sorted(open_ports)}") # muestra los puertos abiertos en orden ascendente
    else:   
        print(f"Puertos cerrados  en {target_ip}")


target = "google.com" # Aqui pones tu direccion
scan_ports_range(target, 75, 85)
     
