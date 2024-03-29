import socket
from cryptography.fernet import Fernet
from decoder import receiveCypher
from encoder import sendCypher


receiveHost = '127.0.0.2'
receivePort = 7001

sendHost = '127.0.0.1'
sendPort = 7000

receiveAddr = (receiveHost, receivePort)
sendAddr = (sendHost, sendPort)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(sendAddr)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

server_socket.bind(receiveAddr)
server_socket.listen(10)
print('Aguardando conexão...')
con, client = server_socket.accept()
print('Conexão estabelecida!')

username = input('Usuario: ')
client_socket.send(username.encode("utf-8"))

print('Aguardando outro usuário...')
otherUser = con.recv(1024).decode("utf-8")

while True:
    sendMSG = input("Envie algo: ")

    if sendMSG == 'TCHAU':
        #client_socket.send(bytes(sendMSG, encoding= 'utf-8'))
        print("Fim de conversa!")
        server_socket.close()
        client_socket.close()
        break
    
    else:
        # Chamar função de encriptar mensagem
        cipherText = sendCypher(sendMSG)

        # Enviar mensagem
        client_socket.send(cipherText)

        print('Aguardando mensagem...')
        receive = con.recv(1024)

        if receive.decode("utf-8") == '':
            print('Conversa encerrada pelo outro usuário!')
            server_socket.close()
            client_socket.close()
            break

        print(otherUser + ": "+" "+ receive.decode("utf-8"))

        # Chamar função de decriptar mensagem. Adicionar chave gerada e passar mensagem encriptada e chave como parâmetro
        receiveMSG = "!-->NÃO DECIFRADO. TENTE NOVAMENTE<--"
        while receiveMSG == "!-->NÃO DECIFRADO. TENTE NOVAMENTE<--":
            print("Decifrando...")
            key = input("Chave: ")
            receiveMSG = receiveCypher(bytes(receive.decode('utf-8'), encoding='utf-8'), key)
            print(otherUser+": "+receiveMSG)
            