import platform
import socket
import psutil
import os

def info_pc(ip_server):
	s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8",80))

	os_name=f"{platform.platform()}\n[*] ARCH: {platform.architecture()[0]} {platform.architecture()[1]}"
	hostname=f"{platform.node()}"
	ip=f"{s.getsockname()[0]}"
	cpu=f"{platform.processor()}"
	if cpu=="":
		cpu="unknown"
	cpu_proc=f"{psutil.cpu_percent(10)}"
	cpu_count=f"{os.cpu_count()}"
	ram_total=f"{round(psutil.virtual_memory()[0]/(2**30),1)}"
	ram_proc=f"{psutil.virtual_memory()[2]}"
	hdd=psutil.disk_usage('/')
	hdd_total=f"{round(hdd.total/(2**30),2)}"
	hdd_used=f"{round(hdd.used/(2**30),2)}"
	hdd_free=f"{round(hdd.free/(2**30),2)}"
	hdd_proc=F"{round(hdd.percent)}"

	print(f"[*] OS: {os_name}")
	print(f"[*] HOSTNAME: {hostname}")
	print(f"[*] IP: {ip}")
	print(f"[*] CPU: {cpu} count:{cpu_count} {cpu_proc}%")
	print(f"[*] RAM: {ram_total}GB {ram_proc}%")
	print(f"[*] HDD/SSD: TOTAL={hdd_total}GB USED={hdd_used}GB FREE={hdd_free}GB {hdd_proc}%")
	print(f"[*] NETWORK: {2+2}")
	print(f"[*] OPEN PORT: {2+2}")

info_pc("work")
