def make_repeater_off(n):
    def repeater(string):
        #afirmo que lo que va llegar es un string, sino devuelvo un error
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string*n
    return repeater

def make_division_by(n):
    #esta funcion lamba recibe como parametro un numero "x" y lo divide por el n del scope superior
    assert n!= 0, "No puedes dividir por cero"
    return lambda x: x/n

def run():
    #en repeater_5 se guarda la funcion repeater que multiplica un string por un enter
    #en este caso el entero se lo paso a la funcion envolvente make_repeater
    repeater_5 = make_repeater_off(5)
    print(repeater_5("Hola"))

    repeater_10 = make_repeater_off(10)
    print(repeater_10("Nahuel"))

    division_by_3 = make_division_by(3)
    print(division_by_3(18))

if __name__ == '__main__':
    run()