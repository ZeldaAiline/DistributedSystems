# echo-client.py

import socket
import argparse

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65431  # The port used by the server
def client(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = input("client >")
        s.sendall(msg.encode())
        print(f"Sent token: <{msg!r}>")

def parse_args():
	parser = argparse.ArgumentParser(
						prog = 'echo-server.py',
						description = 'python program to implement token ring algorithm',
						epilog="example: python %(prog)s --host 127.0.0.1 --port 65431 --host-next 127.0.0.1 --port-next 65432")

	parser.add_argument('--host', nargs='?', default='127.0.0.1', help='host for the current server', const=str)
	parser.add_argument('--port', nargs='?', default=65431, help='port for the current server', const=int)
	args=parser.parse_args()
	#print("the inputs are:")
	#for arg in vars(args):
	#	print("{} is {}".format(arg, getattr(args, arg)))
	return args

def main():
	inputs=parse_args()
	client(inputs.host,inputs.port)



if __name__ == '__main__':
    main()

