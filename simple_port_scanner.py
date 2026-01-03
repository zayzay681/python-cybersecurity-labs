import socket
try:
	t = input ("Enter target IP or host name:").strip()
	start_port = int (input ("Enter start port:"))
	end_port = int (input ("Enter end port:"))
	if start_port < 1 or end_port > 65535 or start_port > end_port:
		print ("invalid port range. use ports 1-65535")
	print (f"\n Scanning {t} from port {start_port} to {end_port}\n")
	for port in range (start_port, end_port +1):
		try:
			a = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
			a.settimeout (1)
			result = a.connect_ex((t, port))
			if result == 0:
				print (f"port {port} is OPEN")
			a.close()
		except socket.error:
			print (f"socket error on port {port}")
			continue
except ValueError:
	print("ports must be numbers only.")
except socket.gaierror:
	print ("invalid hostname or IP address.")
except KeyboardINterrupt:
	print ("scan stopped by user,")
except Exception as e:
	print (f"unexpected error: {e}")
else:
	print ("\n scan complete successfully")
