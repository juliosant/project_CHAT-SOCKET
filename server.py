
import socket
from cryptography.fernet import Fernet

def loadKey():
    return open('secret.key', 'rb').read()
    
def receiveCypher(cypher, isKey):
    if bytes(isKey, encoding="utf-8") == loadKey(): # comparar as chaves
        cipherSuite = Fernet(isKey)   
        plainText = cipherSuite.decrypt(cypher)
        return plainText.decode('utf-8')
    else:
        return "!-->NÃO DECIFRADO<--"

receiveHost = '127.0.0.1'  #ip de origem
receivePort = 7000  #porta de origem
receiveAddr = (receiveHost, receivePort) 

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criando conexão TCP
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  

serv_socket.bind(receiveAddr) #Estado de espera
serv_socket.listen(10)  #limite de conxões
print('aguardando conexao')
con, cliente = serv_socket.accept() #Aceitando a conexão vinda do cliente
print('conectado' )

#Estabelecendo parametros do destino
sendHost = '127.0.0.2' #ip de destino
sendPort = 7001 #porta de destino
sendAddr = (sendHost, sendPort)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criando conexão TCP
client_socket.connect(sendAddr) #solicitando conexão

username = str(input('Usuario: '))
client_socket.send(username.encode("utf-8"))

print('Aguardando outro usuário...')
otherUser = con.recv(1024).decode("utf-8")
#Finalizado estabelecimento de conexão

#Criando conversa

while True:
    print('Aguardando mensagem...')
    receive = con.recv(1024)
    # Decriptando
    
    #print("Descifrando...")
    #key = input("Chave: ")
    #receiveMSG = receiveCypher(bytes(receive.decode('utf-8'), encoding='utf-8'), key)
    #print(otherUser+": "+ receiveMSG)
    #receiveCypher(bytes(receive.decode('utf-8'), encoding='utf-8'), key)

    if receive.decode("utf-8") == '':
        print('Conversa encerrada pelo outro usuário!')
        serv_socket.close()
        client_socket.close()
        break
    
    else:
        print(otherUser+": "+" "+ receive.decode('utf-8'))

        # Decriptando
        print("Descifrando...")
        key = input("Chave: ")
        print(otherUser+": "+receiveCypher(bytes(receive.decode('utf-8'), encoding='utf-8'), key))
        #receiveCypher(bytes(receive.decode('utf-8'), encoding='utf-8'), key)
        
        sendMSG = input("Envie algo: ")
        if sendMSG == 'TCHAU':
            print("Fim de conversa!")
            serv_socket.close()
            client_socket.close()
            break
        
        else:
            sendMSG = bytes(sendMSG, encoding= 'utf-8')
            key = Fernet.generate_key()
            with open('secret.key', 'wb') as keyFile:
                keyFile.write(key)
            cipherSuite = Fernet(key)
            cipherText = cipherSuite.encrypt(sendMSG)
            
            client_socket.send(cipherText)
        
        '''
        sendMSG = bytes(input("Envie algo: "), encoding= 'utf-8')
        key = Fernet.generate_key()
        with open('secret.key', 'wb') as keyFile:
            keyFile.write(key)
        cipherSuite = Fernet(key)
        cipherText = cipherSuite.encrypt(sendMSG)
        
        client_socket.send(cipherText)

        if sendMSG == 'TCHAU':
            print("Fim de conversa!")
            serv_socket.close()
            client_socket.close()
            break
        '''