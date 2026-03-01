from collections import Counter

abecedario = "abcdefghijklmnñopqrstuvwxyz"
letra_a_indice = {letra: i for i, letra in enumerate(abecedario)}
indice_a_letra = {i: letra for i, letra in enumerate(abecedario)}

#########################################################################
# FUERZA BRUTA
#########################################################################

def fuerza_bruta(texto_cifrado):
    texto_cifrado = texto_cifrado.lower()
    for i in range(27):
        texto_descifrado = ""
        for letra in texto_cifrado:
            if letra == " ": 
                texto_descifrado += " "
                continue
            indice = letra_a_indice[letra]
            texto_descifrado += indice_a_letra[(indice -i)%27]
        print("------------------------------------------------------")
        print("n = ", i)
        print(texto_descifrado)


#########################################################################
# CONOCIMIENTO ADICIONAL
#########################################################################

def quitar_acentos(texto):
    reemplazos = {
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u"
    }
    for acentuada, normal in reemplazos.items():
        texto = texto.replace(acentuada, normal)
    return texto

def conocimiento_adicional(texto_cifrado, letra_cifrada, letra_descifrada):
    texto_cifrado = quitar_acentos(texto_cifrado.lower())
    texto_descifrado = ""
    n = (letra_a_indice[letra_cifrada] - letra_a_indice[letra_descifrada]) % 27
    for letra in texto_cifrado:
        if letra == " ":
            texto_descifrado += " "
            continue
        indice = letra_a_indice[letra]
        texto_descifrado += indice_a_letra[(indice -n)%27]
    print("La clave usada fue: ", n)
    print(texto_descifrado)
    return

#########################################################################
# ANÁLISIS DE FRECUENCIAS
#########################################################################

def mayor_frecuencia(texto):
    texto = [c for c in texto if c in abecedario]
    conteo = Counter(texto)
    return conteo.most_common(1)[0][0]

def analisis_frecuencias(texto_cifrado):
    texto_cifrado = texto_cifrado.lower()
    letra_frec = mayor_frecuencia(texto_cifrado)
    conocimiento_adicional(texto_cifrado, letra_frec, "e")

if __name__ == "__main__":
    print("----------------------- Cifrado César -----------------------")
    print("Descifrando la frase Nc xkfc gu dgnnc por fuerza bruta:")
    fuerza_bruta("Nc xkfc gu dgnnc")

    print("\nDescifrando la frase Zo qgweidugotío sh jb hsqgsid por conocimiento adicional:")
    conocimiento_adicional("Zo qgweidugotío sh jb hsqgsid", "d", "o")

    print("\nDescifrando la frase Jx qzd kfhnp mjwnw f ptx ijqfx xnr ifwxj hzjryf xtgwj ytit hzfrit jwjx ñtajr por análisis de frecuencias:")
    analisis_frecuencias("Jx qzd kfhnp mjwnw f ptx ijqfx xnr ifwxj hzjryf xtgwj ytit hzfrit jwjx ñtajr")
