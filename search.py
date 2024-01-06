"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo, y los empates se resuelvan de forma aleatoria.
Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from problem import OptProblem
from node import Node
from random import choice
from time import time


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Crear el nodo inicial
        actual = Node(problem.init, problem.obj_val(problem.init))

        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual.state)

            # Buscar las acciones que generan el  mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local
            if diff[act] <= 0:

                self.tour = actual.state
                self.value = actual.value
                end = time()
                self.time = end-start
                return

            # Sino, moverse a un nodo con el estado sucesor
            else:

                actual = Node(problem.result(actual.state, act),
                              actual.value + diff[act])
                self.niters += 1


class HillClimbingReset(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Crear el nodo inicial
        while self.niters < 3000: 
            actual = Node(problem.init, problem.obj_val(problem.init))
            while True:

                # Determinar las acciones que se pueden aplicar
                # y las diferencias en valor objetivo que resultan
                diff = problem.val_diff(actual.state)

                # Buscar las acciones que generan el  mayor incremento de valor obj
                max_acts = [act for act, val in diff.items() if val ==
                            max(diff.values())]

                # Elegir una accion aleatoria
                act = choice(max_acts)

                # Retornar si estamos en un optimo local
                if diff[act] <= 0:
                    if self.value == None or self.value < actual.value:
                        self.tour = actual.state
                        self.value = actual.value
                        end = time()
                        self.time = end-start
                    problem.random_reset()
                    break

                # Sino, moverse a un nodo con el estado sucesor
                else:

                    actual = Node(problem.result(actual.state, act), actual.value + diff[act])
                    self.niters += 1



class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""

    def solve(self, problem: OptProblem):
            """Resuelve un problema de optimizacion con ascension de colinas.

            Argumentos:
            ==========
            problem: OptProblem
                un problema de optimizacion
            """
            # Inicio del reloj
            start = time()

            actual = Node(problem.init, problem.obj_val(problem.init))
            
            best = actual
            tabu = []
            while self.niters < 3000:
                diff = problem.val_diff(actual.state)
                for key, value in diff.items():
                    if key in tabu:
                        diff[key] = -99999
                #diff = {key: value for key, value in diff.items if key not in tabu}
                max_acts = [act for act, val in diff.items() if val == max(diff.values())]
                act = choice(max_acts)
                if best.value < diff[act]:
                    best = Node(problem.result(best.state, act), best.value + diff[act])
                tabu.append(act)
                actual = Node(problem.result(actual.state, act), actual.value + diff[act])
                self.niters += 1

                if self.value == None or self.value < best.value:
                    self.tour = best.state
                    self.value = best.value
                    end = time()
                    self.time = end-start