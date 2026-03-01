from problema1 import quitar_acentos

alfabeto = "abcdefghijklmnopqrstuvwxy"
cuadrado = {}
inverso = {}

fila = 1
col = 1
for letra in alfabeto:
    coordenada = f"{fila}{col}"
    cuadrado[letra] = coordenada
    inverso[coordenada] = letra 
    col += 1
    if col > 5:
        col = 1
        fila += 1

def descifrar(codigo):
    codigo = codigo.replace(" ", "")
    texto = ""
    for i in range(0, len(codigo), 2):
        par = codigo[i:i+2]
        if par in inverso:
            texto += inverso[par]
    return texto

codigo = "15 32 45 24 15 33 41 35 34 35 15 44 41 15 43 11 11 34 11 14 24 15"

def cifrar(texto):
    texto = quitar_acentos(texto.lower())
    resultado = []
    for letra in texto:
        if letra in cuadrado:
            resultado.append(cuadrado[letra])
    return " ".join(resultado)

frase = "Si la felicidad tuviera una forma, tendría forma de cristal, porque puede estar a tu alrededor sin que la notes. Pero si cambias de perspectiva, puede reflejar una luz capaz de iluminarlo todo"


if __name__ == "__main__":
    print("----------------------- Cuadrado de Polibio -----------------------")
    print("\nDescifrando el código ", codigo)
    print(descifrar(codigo))

    print("\nCifrando la frase ", frase)
    print(cifrar(frase))
    