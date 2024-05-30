def main():
    notas = [18,17,20,16]
    s = slice(0,3,1)
    print(type(s))
    print(notas[s])

    sub_notas = notas[0:3:1]
    print(sub_notas)

def arrays():
    original = [] # inicializando
    original = [1,2,3,4]

    # usando copy
    copia = original.copy()
    original.append(5)
    print(copia)

    # invirtiendo
    invertida = original[::-1]
    print(invertida)

    # eliminando elementos
    del original[0:2]
    print(original)

    # concatenando
    lista_nueva = [10,11,12,13]
    concatenada = original + lista_nueva
    print(concatenada)

def sets():
    fruits = set() #inicializando
    fruits = {'apple','pear','orange','banana'}
    fruits.add('cherry')
    print(fruits)

    #fruits.remove('watermelon') # throws error if the item doesn't exist
    fruits.discard('watermelon') # doesn't throw error if the item doesn't exist
    print(fruits)

def diccionarios():
    person = {} # inicializando
    person = { "name": "Alice", "age": 23, "city": "New York", "name": "Gian"}
    print(person)

    person['email'] = "alice@gmail.com"
    print(person["email"])

    keys = person.keys() # obtener claves
    values = person.values() # obtener valores
    items = person.items()

    print(keys)
    print(values)
    print(items)

    numbers = [1, 2, 3, 4, 5]
    squares_dict = { x: x**2 for x in numbers }
    print(squares_dict)


if __name__ == "__main__":
    diccionarios()
