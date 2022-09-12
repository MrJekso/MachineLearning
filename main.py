import platform
import socket
import psutil
import os
import speedtest
import socket
import datetime

class User_account:
	def __init__(self,firstname, lastname, post, department):
		self.lastname = lastname
		self.firstname = name
		self.post = post
		self.department = department
		self.proc_cpu = ""
		self.proc_memory = ""
		self.proc_ram = ""
		slef.proc_net = ""

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

def info_cpu():
	return psutil.cpu_percent(10)

def info_memory():
	hdd=psutil.disk_usage('/')
	return round(hdd.percent)

def info_ram():
	return round(psutil.virtual_memory()[2])

def info_net():
	servernames = []
	st = speedtest.Speedtest()
	st.get_servers(servernames)
	return round(st.results.ping/(2**20),2)

def config(ip_server):
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
	cpu_proc=f"{info_cpu()}"
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
def cp_config():
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.connect(("8.8.8.8",80))
	ip = s.getsockname()[0]
	cpu = platform.processor()
	cpu_count = os.cpu_count()
	ram = round(psutil.virtual_memory()[0]/(2**30),1)
	hdd = psutil.disk_usage('/')
	hdd_total = round(hdd.total/(2**30),2)
	hdd_used = round(hdd.used/(2**30),2)
	hdd_free = round(hdd.free/(2**30),2)

	data = {"OS":platform.platform(),"ARCH":platform.architecture()[0],
		"ARCH_FILE":platform.architecture()[1],"HOST":platform.node(),
		"IP":ip,"CPU":cpu,"CPU_COUNT":cpu_count,"RAM":ram,
		"HDD_TOTAL":hdd_total,"HDD_USED":hdd_used,"HDD_FREE":hdd_free}
	return data

def cp_down():
	pass
def main(start_word):
	config("127.0.0.1")
	print(cp_config())

main("work")
#commit respect
