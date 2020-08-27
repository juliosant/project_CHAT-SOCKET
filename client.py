import socket

receiveHost = '127.0.0.2'
receivePort = 7001

sendHost = '127.0.0.1'
sendPort = 7000

receiveAddr = (receiveHost, receivePort)
sendAddr = (sendHost, sendPort)

'''ip = input('digite o ip de conexao: ')
port = 7000
addr = ((ip,port))
'''
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(sendAddr)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

server_socket.bind(receiveAddr)
server_socket.listen(10)
print('Aguardando conexão...')
con, client = server_socket.accept()
print('Conexão estabelecida!')

'''mensagem = input("digite uma mensagem para enviar ao servidor")
client_socket.send(mensagem.encode('utf-8'))
print('mensagem enviada')
client_socket.close()
'''
username = input('Usuario: ')
client_socket.send(username.encode("utf-8"))

print('Aguardando outro usuário...')
otherUser = con.recv(1024).decode("utf-8")

while True:
    sendMSG = input("Envie algo: ")
    client_socket.send(sendMSG.encode('utf-8'))

    if sendMSG == 'TCHAU':
        print("Fim de conversa!")
        server_socket.close()
        client_socket.close()
        break
    
    else:
        print('Aguardando mensagem...')
        receive = con.recv(1024)
        print(otherUser + ": "+" "+ receive.decode("utf-8"))

        if receive.decode('utf-8') == 'TCHAU':
            print('Conversa encerrada pelo outro usuário!')
            server_socket.close()
            client_socket.close()
            break