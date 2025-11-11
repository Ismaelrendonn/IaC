from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

def generar_clave_y_iv():

      # GENERA UNA CLAVE AES DE 32 BYTES (256 BITS) Y UN IV DE 16 BYTES (128 BITS)
    key = urandom(32)# 32 bytes para AES-256
    iv = urandom(16)# 16 bytes para el IV de AES

    return key, iv

def encriptar(texto_plano, key, iv):

    # CREA UN OBJETO CIPHER PARA AES EN MODO CBC
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    #PADDING PARA QUE EL TEXTO TENGA UNA LONGITUD QUE SEA MULTIPLE DE TAMAÑO DE BLOQUES 
    texto_plano_bytes = texto_plano.encode('utf-8')
    padding_length = 16 - (len(texto_plano_bytes) % 16) 
    padding = bytes([padding_length] * padding_length)
    texto_a_cifrar = texto_plano_bytes + padding
   
    texto_cifrado =encryptor.update(texto_a_cifrar) + encryptor.finalize()
    return texto_cifrado

def desencriptar(texto_cifrado, key, iv):
    cipher= Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    texto_desencriptado_con_padding = decryptor.update(texto_cifrado) + decryptor.finalize()

    padding_length = texto_desencriptado_con_padding[-1]
    texto_desencriptado = texto_desencriptado_con_padding[:-padding_length]
    return texto_desencriptado.decode('utf-8')

key,iv = generar_clave_y_iv()
texto_original = "Diego Ismael Rendon Alonso"

texto_encriptado =encriptar(texto_original, key, iv)
print(f"Texto Encriptado: {texto_encriptado}")
texto_desencriptado = desencriptar(texto_encriptado, key, iv)
print(f"Texto Desencriptado: {texto_desencriptado}")