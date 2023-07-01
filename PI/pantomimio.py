import string
def pantograma():
    frase = input()
    frase.replace(" ", "").lower()
    frase = ''.join(filter(str.isalpha, frase))
    alfabeto = set(string.ascii_lowercase)
    letras_frase = set(frase)
    if letras_frase == alfabeto:
        print("SIM")
    else:
        print("NAO")


pantograma()

