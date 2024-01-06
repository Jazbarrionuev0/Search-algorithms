"""Este modulo se encarga de la lectura de archivos ".tsp".

Requiere del paquete tsplib95.
"""

from __future__ import annotations
from tsplib95 import load
from networkx import Graph


def read_tsp(filename: str) -> tuple[Graph, dict[int, tuple[int, int]]]:
    """Lee un archivo en formato ".tsp".

    Argumentos:
    ==========
    filename: str
        ruta de la instancia

    Retorna:
    =======
    G: Graph
        grafo con los datos del TSP
    coords: dict[int, tuple[int, int]]
        diccionario con las coordenadas de cada ciudad.
    """
    problem = load(filename)
    coords = problem.node_coords
    G = problem.get_graph()
    return G, coords
