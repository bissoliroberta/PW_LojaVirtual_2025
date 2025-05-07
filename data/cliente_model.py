from dataclasses import dataclass


@dataclass
class Cliente:
    id: int
    nome: str
    CPF: int
    email: str
    telefone: int
    senha: str