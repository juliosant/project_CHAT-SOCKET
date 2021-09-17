from cryptography.fernet import Fernet # para chavs simétrica

def receiveCypher(cypher, key):
    try:
        cipherSuite = Fernet(key) # criar variável Fernet para a chave
        plainText = cipherSuite.decrypt(cypher) # Usando a chave para decriptar a mensagem
        return plainText.decode('utf-8') # Retornar mensagem decifrada
    except: # Em caso de chave errada será gerado um erro. Nesse caso, a exceção é mostrada.
        return  "!-->NÃO DECIFRADO. TENTE NOVAMENTE<--"