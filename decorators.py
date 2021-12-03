from datetime import datetime

def execution_time(func):
    #no importa la cantidad de argumentos posicionales o nombrados, la funcion los recibe igual
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time = final_time - initial_time
        print("Pasaron " + str(time.total_seconds()) + " segundos")
    return wrapper

@execution_time
def random_func():
    #cuando no me interesa la variable que va iterando utilizo _
    for _ in range(1 ,1000000):
        pass

@execution_time
def suma (a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre="Nahuel"):
    print("Hola " + nombre)

random_func()
suma(3,4)
saludo()