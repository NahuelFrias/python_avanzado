def is_prime(number: int) -> bool:
    results_list = [x for x in range(2, number) if number % x == 0]
    return len(results_list) == 0

def run():
    number: int = int(input("Ingrese un numero: "))
    number_is_prime: bool = is_prime(number)
    print(f'Is {number} a prime number? {number_is_prime}')


if __name__ == '__main__':
    run()