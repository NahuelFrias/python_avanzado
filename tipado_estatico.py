from typing import Dict, List, Tuple
#esta libreria ayuda a trabajar con un tipado fuerte

a : int = 5
print (a)

def suma(a:int, b:int) -> int:
    return a + b

print(suma("1","2"))


positives: List[int] = [1,2,3]
users : Dict[str, int] = {
    "argentina" : 1,
    "bolivia" : 2,
    "chile" : 3
}

countries: List[Dict[str,str]] = [
    {
        "name" : "argentina",
        "people" : "45000000"
    }
    {
        "name" : "brasil",
        "people" : "200000000"
    }
]

numbers: Tuple [int, float, int] = (1, 3.5, 99)