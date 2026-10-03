import hashlib
import secrets

ITERACIONES = 120_000
LONGITUD_SAL = 16
ALFABETO = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"


def generar_sal() -> str:
    return secrets.token_hex(LONGITUD_SAL)


def hashear(clave: str, sal: str) -> str:
    derivada = hashlib.pbkdf2_hmac(
        "sha256",
        clave.encode("utf-8"),
        sal.encode("utf-8"),
        ITERACIONES,
    )
    return derivada.hex()


def verificar(clave: str, sal: str, hash_esperado: str) -> bool:
    if not hash_esperado:
        return False
    return secrets.compare_digest(hashear(clave, sal), hash_esperado)


def generar_clave(longitud: int = 8) -> str:
    return "".join(secrets.choice(ALFABETO) for _ in range(longitud))