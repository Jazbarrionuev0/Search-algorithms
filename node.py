"""Este modulo contiene la clase Node.

Node representa un nodo para una busqueda local, es decir,
almacena un estado su un valor objetivo.
"""
from typing import TypeVar

State = TypeVar('State')
Action = TypeVar('Action')


class Node:
    """Clase que representa un nodo para busqueda local."""

    def __init__(self, state: State, value: float) -> None:
        """Construye una instancia de la clase.

        Argumentos:
        ==========
        state: State
            un estado
        value: float
            un valor objetivo
        """
        self.state = state
        self.value = value

    def __repr__(self):
        """Representacion de nodos."""
        return "<Node {}>".format(self.state)

    def __eq__(self, other):
        """Nocion de igualdad nodos."""
        return isinstance(other, Node) and self.state == other.state

    def __lt__(self, node):
        """Nocion de comparacion de nodos."""
        return self.state < node.state
