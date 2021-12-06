#union
my_set1 = {1,2,3}
my_set2 = {3,4,5}
my_set3= my_set1 | my_set2
print(my_set3)
#interseccion
my_set4 = my_set1 & my_set2
print(my_set4)
#diferencia
my_set5 = my_set1 - my_set2
print(my_set5)
#diferencia simetrica
my_set6 = my_set1 ^ my_set2
print(my_set6)


#eliminar elementos duplicados

def remove_duplicates(list):
    without_duplicates = []
    for elements in list:
        if elements not in without_duplicates:
            without_duplicates.append(elements)
    return without_duplicates

#mas efectivo
def remove_duplicates_with_sets(some_list):
    return list(set(some_list))


def run():
    random_list = [1,1,2,2,4]
    print(remove_duplicates(random_list))
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    run()