import platform
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8",80))

os=f"{platform.system()} {platform.architecture()[0]} {platform.architecture()[1]}"
hostname=f"{platform.node()}"
ip=f"{s.getsockname()[0]}"

print(f"[*] OS: {os}")
print(f"[*] HOSTNAME: {hostname}")
print(f"[*] IP: {ip}")
print(f"[*] CPU: {2+2}")
print(f"[*] RAM: {2+2}")
print(f"[*] HHD/SSD: {2+2}")
print(f"[*] NETWORK: {2+2}")
print(f"[*] OPEN PORT: {2+2}")

