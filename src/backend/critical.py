import sympy.core
from networkx.algorithms.polynomials import tutte_polynomial

from backend.graph_utils import Graph


def build(n: int, m: int, g: Graph) -> sympy.core.Expr:
    """
    Build a Critical configuration polynomial for graph G.
    Params n and m are accepted for similar declaration
    :param n: number of vertex in graph [ignored]
    :param m: number of edges in graph [ignored]
    :param g: graph to analyse
    :return:
    Critical configuration polynomial for graph g. See more at
    https://link.springer.com/article/10.1134/S1560354717080032
    """
    nxg = g.to_networkx()
    poly = tutte_polynomial(nxg)
    poly = poly.subs("x", 1)
    poly = poly.subs("y", "x")
    return poly
