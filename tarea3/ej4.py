import hashlib
import math
import unicodedata
import string
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# ---------------------------------------------------------
# FUNCIONES AUXILIARES
# ---------------------------------------------------------
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def derive_key(key):
    """Deriva la clave a 32 bytes usando SHA-256 para AES-GCM."""
    return hashlib.sha256(key.encode()).digest()


def decrypt_gcm(data, key):
    key_bytes = derive_key(key)
    aesgcm = AESGCM(key_bytes)
    nonce = data[:12]
    ciphertext = data[12:]
    return aesgcm.decrypt(nonce, ciphertext, None).decode()


# ---------------------------------------------------------
# CONSTRUCCIÓN DE LA CLAVE
# ---------------------------------------------------------
def construir_clave(texto_crudo):
    texto_normalizado = unicodedata.normalize('NFKD', texto_crudo).encode('ASCII', 'ignore').decode('utf-8')
    texto_filtrado = ''.join(c for c in texto_normalizado if c in string.ascii_letters).lower()
    longitud = len(texto_filtrado)

    caracteres_extraidos = ""
    num = 2
    while len(caracteres_extraidos) < 25:
        if es_primo(num):
            indice = (num - 2) % longitud
            caracteres_extraidos += texto_filtrado[indice]
        num += 1

    palabra_base = "kevinmitnick"
    clave_final = ""
    for i in range(25):
        clave_final += caracteres_extraidos[i]
        clave_final += palabra_base[i % len(palabra_base)]

    return clave_final


# ---------------------------------------------------------
# EJECUCIÓN PRINCIPAL
# ---------------------------------------------------------
def main():
    with open('file.txt', 'r', encoding='utf-8') as f:
        texto_crudo = f.read()

    with open('hashes.txt', 'r') as f:
        hashes_validos = [line.strip() for line in f.readlines()]

    with open('cipher.txt', 'r') as f:
        cipher_hex = f.read().replace('\n', '').strip()

    clave_candidata = construir_clave(texto_crudo)
    print(f"\nClave candidata generada: {clave_candidata}")

    hash_candidato = hashlib.sha256(clave_candidata.encode()).hexdigest()
    print(f"\nHash de la clave: {hash_candidato}")

    if hash_candidato in hashes_validos:
        print("\nHubo un match con un hash en hashes.txt")

        try:
            cipher_bytes = bytes.fromhex(cipher_hex)
            key_bytes = hashlib.sha256(hash_candidato.encode()).digest()  
            aesgcm = AESGCM(key_bytes)
            mensaje = aesgcm.decrypt(cipher_bytes[:12], cipher_bytes[12:], None).decode()
            print("\nMensaje descifrado:")
            print(mensaje)
        except Exception as e:
            print(f"Error al descifrar: {e}")
    else:
        print("El hash de la clave no coincide con ninguno en hashes.txt.")


if __name__ == "__main__":
    main()