"""Este modulo se encarga de graficar los tours.

Requiere del paquete matplotlib.
"""

from __future__ import annotations
import matplotlib.pyplot as plt
import networkx as nx


def show(G: nx.Graph,
         coords: dict[int, tuple[float, float]],
         name: str,
         sols: dict[str, tuple[list[int]], float]) -> None:
    """Grafica un conjunto de tours.

    Argumentos:
    ==========
    G: nx.Graph
        grafo que representa la instancia del TSP
    coords: dict[int, tuple[float, float]]
        diccionario con las coordenadas de cada ciudad
    name: str
        nombre de la instancia
    sols: dict[str, tuple[list[int]], float]
        diccionario con el tour y su costo para cada algoritmo de busqueda
    """
    # Crear los subplots
    fig, axs = plt.subplots(nrows=1, ncols=len(sols))

    # Determinar colores
    colors = plt.rcParams["axes.prop_cycle"]()

    for i, algo in enumerate(sols):

        # Recuperar el tour y su valor objetivo
        tour, val = sols[algo]

        # Dibujar los nodos
        nx.draw_networkx_nodes(G, pos=coords, node_size=10,
                               ax=axs[i], node_color="black")

        # Dibujar las aristas del tour
        tour = [i+1 for i in tour]
        edges = list(zip(tour, tour[1:]))
        nx.draw_networkx_edges(G, pos=coords, edgelist=edges,
                               ax=axs[i], label="{}: {}".format(algo, val),
                               edge_color=next(colors)["color"])

        axs[i].legend()

    # Mostrar la grafica
    fig.suptitle(name, fontsize=15)
    plt.subplots_adjust(hspace=0.5)
    plt.show()
