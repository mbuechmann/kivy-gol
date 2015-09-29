import random

class Population:

    rows = None
    cols = None
    cells = None
    _propability = 0.3

    def __init__(self, cols=100, rows=100):
        self.rows = rows
        self.cols = cols
        self.cells = [[self._init_cell(col, row) for row in range(rows)] for col in range(cols)]

    def evolve(self):
        next_gen = [[self._evolve_cell(col, row) for row in range(self.rows)] for col in range(self.cols)]
        self.cells = next_gen

    def _init_cell(self, x, y):
        return random.random() < self._propability

    def _value_at(self, x, y):
        return self.cells[x % self.cols][y % self.rows]

    def _neighbor_count(self, x, y):
        res = 0

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (dx != 0 or dy != 0) and self._value_at(x + dx, y + dy):
                    res += 1

        return res

    def _evolve_cell(self, x, y):
        if self._value_at(x, y):
            return self._neighbor_count(x, y) in (2, 3)
        else:
            return self._neighbor_count(x, y) == 3
