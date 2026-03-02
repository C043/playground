from mazesForProgrammers.gridClasses.Cell import Cell


class Grid:
    def __init__(self, rows: int, columns: int):
        self.rows: int = rows
        self.columns: int = columns
        self.grid = self.prepareGrid()

    def prepareGrid(self) -> list[list[Cell]]:
        grid = []

        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                row.append(Cell(i, j))
            grid.append(row)

        return grid
