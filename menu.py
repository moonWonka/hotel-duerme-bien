from login import logIn

def menu():

    print("""
    Bienvenido al sistema de registro de pasajeros funte de los deseos
    ingrese sus credenciales  
    """)

    entrar =  logIn()

    if entrar:
        print('wolo')
    else:
        print('error')

    


menu()