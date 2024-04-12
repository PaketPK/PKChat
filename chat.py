_A='utf-8'
import socket,threading
def receive_messages(client_socket):
	while True:
		try:A=client_socket.recv(1024).decode(_A);print(A)
		except:break
def main():
	C=input('Enter your nickname: ');A=socket.socket(socket.AF_INET,socket.SOCK_STREAM);A.connect(('offers-visits.gl.at.ply.gg',25025));A.send(C.encode(_A));D=threading.Thread(target=receive_messages,args=(A,));D.daemon=True;D.start()
	try:
		while True:
			B=input()
			if B.lower()=='exit':A.send(B.encode(_A));break
			A.send('{}: {}'.format(C,B).encode(_A))
	except KeyboardInterrupt:A.close()
if __name__=='__main__':main()