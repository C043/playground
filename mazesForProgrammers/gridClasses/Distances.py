from __future__ import annotations
from typing import List
from mazesForProgrammers.gridClasses.Cell import Cell
from mazesForProgrammers.gridClasses.MaxDistanceResult import MaxDistanceResult


class Distances:
    def __init__(self, root: Cell):
        self.root: Cell = root
        self.cells: dict[Cell, int] = {}
        self.cells[root] = 0

    def get(self, cell: Cell) -> int:
        return self.cells.get(cell, False)

    def put(self, cell: Cell, distance: int):
        self.cells[cell] = distance

    def getCells(self) -> List[Cell]:
        return list(self.cells.keys())

    def pathTo(self, goal: Cell) -> Distances:
        current: Cell = goal
        breadcrumbs: Distances = Distances(self.root)
        breadcrumbs.put(current, self.cells.get(current, 0))

        while current != self.root:
            nextCell = None
            for neighbor in current.getLinks():
                if self.cells.get(neighbor, -1) < self.cells.get(current, -1):
                    nextCell = neighbor
                    break

            if nextCell is None:
                break

            breadcrumbs.put(nextCell, self.cells.get(nextCell, 0))
            current = nextCell

        return breadcrumbs

    def maxDistance(self) -> MaxDistanceResult:
        maxDistance: int = 0
        maxCell: Cell = self.root

        for cell in self.cells:
            distance: int = self.cells[cell]

            if distance > maxDistance:
                maxCell = cell
                maxDistance = distance

        return MaxDistanceResult(maxCell, maxDistance)
