def vizinhos():
    entrada = int(input())
    list = []
    for i in range(0, entrada):
        elemento = int(input())
        list.append(elemento)
    for j in range(0, len(list)-1):
        if list[j] == list[j+1]:
            print(f"Pos {j} e {j+1}")
    

vizinhos()