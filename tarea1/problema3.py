import re
from collections import defaultdict
from collections import Counter

def limpiar_texto(texto):
    return re.sub(r'[^A-Z]', '', texto.upper())


def encontrar_repeticiones(texto, longitud=3):
    posiciones = defaultdict(list)
    
    for i in range(len(texto) - longitud):
        secuencia = texto[i:i+longitud]
        posiciones[secuencia].append(i)
    
    repetidos = {seq: pos for seq, pos in posiciones.items() if len(pos) > 1}
    return repetidos

def calcular_distancias(repetidos):
    distancias = []
    
    for posiciones in repetidos.values():
        for i in range(len(posiciones)-1):
            distancia = posiciones[i+1] - posiciones[i]
            distancias.append(distancia)
    
    return distancias

def divisores(n):
    resultado = []
    for i in range(2, n+1):
        if n % i == 0:
            resultado.append(i)
    return resultado



def posibles_longitudes(distancias):
    todos_divisores = []
    
    for d in distancias:
        todos_divisores.extend(divisores(d))
    
    conteo = Counter(todos_divisores)
    return conteo.most_common(3)

mensaje = """ECISCRVSWVLGDDWUEFHFNGESXUVTICOKQOTA.JPHWAKFBNA
EUONOJFHONCPHRZNSCOKEWLSUFPFEEUWOMHPQFAEEDOLDB
QROKFZLNQBSXVMFZZNMQQSACESDDVMONHBROUEBGMOCVI
SLZAOXDGTJDAQVZLDRTOVAKDDWOKJTFEJBBFNHBGLCRJRLS
KVEVUDBXOPVDVZADBGSLCPOKUWSSJCRQWCOLFOKUC"""

if __name__ == "__main__":
    print("----------------------- Cifrado Vigènere -----------------------")
    texto = limpiar_texto(mensaje)
    repetidos = encontrar_repeticiones(texto)
    distancias = calcular_distancias(repetidos)
    print(f"Secuencias repetidas encontradas: {list(repetidos.keys())}")
    print("\nLongitudes de clave más probables (Longitud, Frecuencia):")
    resultados = posibles_longitudes(distancias)
    for long, freq in resultados:
        print(f"Longitud posible: {long} (aparece como divisor {freq} veces)")