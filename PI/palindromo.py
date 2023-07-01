def palindromo():
    frase = input()
    frase = frase.replace(" ", "").lower()
    if frase == ''.join(reversed(frase)):
        print("PALINDROMO")
    else:
        print("NAO EH PALINDROMO")


palindromo()
