from cryptography.fernet import Fernet # para chavs simétrica

def sendCypher(sendMSG):
    sendMSG = bytes(sendMSG, encoding= 'utf-8') # converter mensagem em bytes
    key = Fernet.generate_key() # Criar chave aleatória
    with open('secret.key', 'wb') as keyFile: # Gerar arquivo 'secrete.key'
        keyFile.write(key) # Escrever chave aleatória dentro do arquivo gerado
    cipherSuite = Fernet(key) # criar variável fernet para a chave
    return cipherSuite.encrypt(sendMSG) # retornar mensagem encriptada