#cifrar en md5
import hashlib

def cifrar(password):
    hashlib_obj = hashlib.md5()
    hashlib_obj.update(password.encode('utf-8'))
    cifrado = hashlib_obj.hexdigest()
    #print(cifrado, len(cifrado))
    return cifrado



#menu()
#menuAdmin()
#menuEncargado()
