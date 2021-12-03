# hago el string de tipado estatico y devuelvo un booleano
def is_palindrome(string: str) -> bool:
    # remplazo los espacios vacias por una cadena vacia y lo pongo en minusculas
    string = string.replace(" ", "").lower()
    # retorno la comparacion del string con el string dado vuelta
    return string == string[::-1]


def run():
    print(is_palindrome(1000))

if __name__ == '__main__':
    run()
