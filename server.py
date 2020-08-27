import socket 

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

'''print( "aguardando mensagem" )
recebe = con.recv(1024) 
print( "mensagem recebida: "+ recebe.decode("utf-8") )
serv_socket.close()
'''

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
    print(otherUser+": "+" "+ receive.decode('utf-8'))

    if receive.decode('utf-8') == 'TCHAU':
        print('Conversa encerrada pelo outro usuário!')
        serv_socket.close()
        client_socket.close()
        break
    
    else:
        sendMSG = input("Envie algo: ")
        client_socket.send(sendMSG.encode('utf-8'))

        if sendMSG == 'TCHAU':
            print("Fim de conversa!")
            serv_socket.close()
            client_socket.close()
            break