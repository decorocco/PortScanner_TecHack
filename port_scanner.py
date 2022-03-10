import socket

ip_host = input("Endereço de IP(IPv4): ")
port_range = input("Range das portas ([ínicio-fim] ex: 21-80): ")

ranges = []
ranges = port_range.split('-')

print("Serviços em portas abertas:")
print(" ")

for i in range(int(ranges[0]), int(ranges[1])):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if conn.connect_ex((ip_host, i)) == 0:
        n_serv = socket.getservbyport(i, "tcp") 
        print(f"port {i}: {n_serv}")
    conn.close()

print("Conexão terminada")

#104.16.44.99