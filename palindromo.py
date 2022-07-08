def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    return palabra == palabra_invertida


def run():
    palabra = input("Escribe la palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print("No es paliíndromo")


if __name__ == '__main__':
    run()

