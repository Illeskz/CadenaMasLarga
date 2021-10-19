
def data():
    array = []
    lenght_array = []
    print("Hola, Encontraré la cadena mas larga que ingreses dentro de un arreglo" )
    array_size = int(input("Por favor ingresa el tamaño del arreglo:  "))
    for i in range(array_size):
        print("Agregar la cadena {}".format(i+1))
        string = input()
        array.append(string)
    print(array)
    return array

def busqueda(array):
    longest_string = array[0]
    equal_size = []
    for i in array:
        if len(longest_string) >= len(i):
            longest_string = longest_string
        # elif len(longest_string) == len(i):
        #     equal_size.append(array.index(i))
        #     longest_string = longest_string
        else:
            longest_string = i
    print("Los indices de las cadenas mas largas son = {}".format(equal_size))
    print("El indice de la cadena mas larga es = {}".format(array.index(longest_string)))


if __name__ == '__main__':
    datos = data()
    busqueda(datos)