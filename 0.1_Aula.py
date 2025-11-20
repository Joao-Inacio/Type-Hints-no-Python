# Tipos básicos
from typing import Final

nome: str = "João"
x: int = 22
y: float = 23.33
c: complex = 3 + 4j
is_valid: bool = True
data: bytes = b"whatever"


# Constates
CONSTANTES = "valor constantes"

# Coleções
lista_numeros: list[int] = [1, 2, 3]
tupla_dois_valores: tuple[str, int] = ("Valor", 234)
tupla_varios: tuple[str, ...] = "a", "b", "c", "..."
conjunto: set[int] = {1, 2, 3, 4}
conjunto_imutavel: frozenset[int] = frozenset([2, 3, 4, 5])
dicionario: dict[str, str] = {"chave": "valor", "chave2": "valor2"}
numeros: range = range(10)

# Outros tipos
nada: None = None
qualquer_coisa: object = "123"
tipo: type[str] = str

# Constantes
CONSTANTES_DOIS: Final[list[str]] = ["a", "b"]
constante_tres: Final[dict[str, int]] = {"valor1": 123, "valor2": 321}
