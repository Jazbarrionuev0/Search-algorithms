"""Este modulo se encarga del parseo de la linea de comandos."""

from argparse import ArgumentParser


def parse() -> ArgumentParser:
    """Parsea la linea de comandos.

    Utiliza el paquete de python argparse.
    """
    # Inicializamos el parser
    parser = ArgumentParser(
        prog='tsp',
        description='This program solves the TSP with different local search \
                     algorithms.',
    )

    # Agregamos los argumentos posicionales
    parser.add_argument('filename',
                        metavar='filename.tsp',
                        help='path to input file')

    return parser.parse_args()
