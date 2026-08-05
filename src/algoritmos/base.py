from typing import Any
from abc import  abstractmethod, ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class KeyPair():
    chave_public: Any
    chave_privada: Any

class AlgoritmoBase(ABC):

    name: str

    @abstractmethod
    def gerar_chaves(self) -> KeyPair:
        pass

    @abstractmethod
    def cifrar(self, texto: bytes, chave_publica : Any) -> Any:
        pass

    @abstractmethod
    def decifrar(self, texto_cifrado: Any, chave_privada: Any) -> bytes:
        pass

    def tamanho_texto_cifrado(self,texto_cifrado: Any, chave_publica: Any | None = None) -> int:
        return len(texto_cifrado)