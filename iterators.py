import time


class FiboIter():

    # construtor
    # le paso un numero maxima para asi elevar la excepcion stopIteration
    def __init__(self, max_number: int):
        self.max_number = max_number

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):

        if self.counter == 0:
            self.counter += 1
            return self.n1

        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # ahora n1 y n2 valen n2 y aux respectivamente
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux

        if self.aux >= self.max_number:
            raise StopIteration

        self.n1, self.n2 = self.n2, self.aux
        self.counter += 1
        return self.aux


if __name__ == '__main__':
    # instancio
    fibonacci = FiboIter(10)

    for element in fibonacci:
        print(element)
        # esto es para ver un poco mas lento el ciclo en el terminal
        time.sleep(0.05)
