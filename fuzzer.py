#!/usr/bin/env python

import socket,time, sys


def fuzzer(host,port,interval=100,timeout=5):
	payload = "A"*100
	#checking if host is up
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.settimeout(5)
		sock.connect((host,port))
		sock.recv(1024)
	except:
		print('{}:{} is not up.\nExiting program...'.format(host,port))
		sys.exit(0)

	#fuzzing
	while True:
		try:
			print('Fuzzing with {} bytes'.format(len(payload)))
			sock.send(payload)
			sock.rev(1024)
			payload += "A"*interval
			time.sleep(1)

		except:
			print('Fuzzing crashed at {} bytes.'.format(len(payload)))
			sys.exit(1)

if __name__=='__main__':
	fuzzer(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
