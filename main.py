import platform
import socket
import psutil
import os
import speedtest
import socket
import datetime

def scan_ports(min_port,max_port):
	ports=[]
	for port in range(min_port, max_port):
		sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		try:
			connect = sock.connect(("127.0.0.1",port))
			ports.append(port)
			sock.close()
		except:
			pass
	return ports

def info_pc(ip_server):
	start = datetime.datetime.now()

	st = speedtest.Speedtest()

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
	net_download=round(st.download()/(2**20),2)
	net_upload=round(st.upload()/(2**20),2)
	servernames=[]
	st.get_servers(servernames)
	net_ping=round(st.results.ping/(2**20),2)
	ports_list=scan_ports(0,10000)
	port_str = ""
	for port in ports_list:
		port_str+=str(port)+" "

	print(f"[*] OS: {os_name}")
	print(f"[*] HOSTNAME: {hostname}")
	print(f"[*] IP: {ip}")
	print(f"[*] CPU: {cpu} count:{cpu_count} {cpu_proc}%")
	print(f"[*] RAM: {ram_total}GB {ram_proc}%")
	print(f"[*] HDD/SSD: TOTAL={hdd_total}GB USED={hdd_used}GB FREE={hdd_free}GB {hdd_proc}%")
	print(f"[*] NETWORK: DOWNLOAD:{net_download}MB UPLAOD:{net_upload}MB PING:{net_upload}MB")
	print(f"[*] OPEN PORT: {port_str}")

	ends = datetime.datetime.now()
	print(f"[*] TIME: {ends-start}")
info_pc("work")
