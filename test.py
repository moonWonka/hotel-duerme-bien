#cifrar en sha256
import hashlib

def cifrar(password):
    hashlib_obj = hashlib.sha256()
    hashlib.update(password.encode('utf-8'))
    cifrado = hashlib_obj.hexdigest()
    return cifrado.hexdigest()


#menu()
#menuAdmin()
#menuEncargado()
