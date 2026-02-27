import socket

target = input("Enter the IP or URL:")
port = 22

print(f"Connecting to {target} on port {port}...")

try:
    s = socket.socket()
    s.settimeout(5)
    s.connect((target, port))

    banner = s.recv(1024)
    result = banner.decode().strip()

    print("\n--- BANNER FOUND ---")
    print(result)

    with open("banners.txt", "a") as file:
        file.write(f"Target: {target} | Banner: {result}\n")

    print("--- Success! Info saved to banners.txt ---\n")   

    s.close()

except Exception as e: 
    print(f"Connection Failed: {e}")
         