# echo-server.py

import socket
import argparse



def send_token(token, HOST,PORT):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		token = int(token) + 1
		s.sendall(str(token).encode())
		print(f"Sent to host {HOST!r} with port {PORT!r} message: <{data!r}>")

def server(HOST,PORT, NEXT_HOST,NEXT_PORT):
	while(True):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			print(f"Binding to host {HOST} with port {PORT}") 
			s.bind((HOST, PORT))
			s.listen()
			conn, addr = s.accept()
			with conn:
				print(f"Connected by {addr}")
				while (True):
					data = conn.recv(1024)
					if not data:
						break
					else: 
						print(f"Received message {data.decode()}")

					send_token(data, NEXT_HOST, NEXT_PORT)


def parse_args():
	parser = argparse.ArgumentParser(
						prog = 'echo-server.py',
						description = 'python program to implement token ring algorithm',
						epilog="example: python %(prog)s --host 127.0.0.1 --port 65431 --host-next 127.0.0.1 --port-next 65432")

	parser.add_argument('--host', nargs='?', default='127.0.0.1', help='host for the current server', const=str)
	parser.add_argument('--port', nargs='?', default=65431, help='port for the current server', const=int)
	parser.add_argument('--host-next', nargs='?', default='127.0.0.1', help='host for the next node/server', const=str)
	parser.add_argument('--port-next',nargs='?', default=65432, help='port for the next node/server', const=int)
	args=parser.parse_args()
	#print("the inputs are:")
	#for arg in vars(args):
	#	print("{} is {}".format(arg, getattr(args, arg)))
	return args

def main():
	inputs=parse_args()
	server(inputs.host,inputs.port,inputs.host_next,inputs.port_next )					


if __name__ == '__main__':
    main()
