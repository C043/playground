from __future__ import annotations
from collections.abc import Collection
from typing import List

from mazesForProgrammers.gridClasses.Distances import Distances


class Cell:
    def __init__(self, row: int, column: int) -> None:
        self.row: int = row
        self.column: int = column
        self.north: Cell
        self.south: Cell
        self.east: Cell
        self.west: Cell
        self.links: dict[Cell, bool] = {}

    def isLinked(self, other: Cell) -> bool:
        return self.links.get(other, False)

    def link(self, other: Cell, bidi: bool):
        self.links[other] = True
        if bidi:
            other.link(self, False)

    def unlink(self, other: Cell, bidi: bool):
        self.links.pop(other, None)
        if bidi:
            other.unlink(self, False)

    def getLinks(self) -> Collection[Cell]:
        return self.links.keys()

    def getNeighbors(self) -> List[Cell]:
        list: List[Cell] = []
        if self.north:
            list.append(self.north)
        if self.south:
            list.append(self.south)
        if self.west:
            list.append(self.west)
        if self.east:
            list.append(self.east)
        return list

    def setLinks(self, links: dict[Cell, bool]):
        self.links = links

    def distances(self) -> Distances:
        distances: Distances = Distances(self)
        frontier: List[Cell] = []
        frontier.append(self)

        while frontier:
            current: Cell = frontier.pop()

            for neighbor in current.getLinks():
                if distances.get(neighbor) == None:
                    distances.put(neighbor, distances.get(current) + 1)
                    frontier.append(neighbor)

        return distances
