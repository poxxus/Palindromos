substituitos = [0, 8, 9, 7, 3, 1, 2, 6, 4, 5]

user_input = str(input())

while user_input != "0":
    list_of_ints = [int(x) for x in user_input]

    result_list = []

    for elemento_lista_entrada in list_of_ints:
        result_list.append(substituitos[elemento_lista_entrada])

    print(''.join(map(str, result_list)))

    user_input = str(input())
