import socket

target = "google.com"

ports = [21, 22, 80, 443, 8080]

print(f"scanning {target}...")

for p in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(1)

    result = client.connect_ex((target, p))

    if result == 0:
        print(f"Port {p}: OPEN")
    else:
        print(f"Port {p}: CLOSED")
    
    client.close()

print("Scan complete.")