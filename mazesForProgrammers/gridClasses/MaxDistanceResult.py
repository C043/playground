from typing import NamedTuple

from mazesForProgrammers.gridClasses.Cell import Cell


class MaxDistanceResult(NamedTuple):
    cell: Cell
    distanc: int
