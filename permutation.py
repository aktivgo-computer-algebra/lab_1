from __future__ import annotations
import lcm


class Permutation:
    length = 0
    elements = []

    def __init__(self, length: int, elements: list):
        self.length = length
        self.elements = elements

    def get_neural_permutation(self) -> Permutation:
        elements = []
        for i in range(0, self.length):
            elements.append(self.elements[i])

        return Permutation(self.length, elements)

    def get_composition(self, perm: Permutation) -> Permutation:
        elements = []
        for i in range(0, self.length):
            elements.append(perm.elements[self.elements[i] - 1])

        return Permutation(self.length, elements)

    def get_reverse_permutation(self) -> Permutation:
        elements = []
        for i in range(0, self.length):
            elements.append(0)

        for i in range(0, self.length):
            elements[self.elements[i] - 1] = i + 1

        return Permutation(self.length, elements)

    def get_degree_permutation(self, n: int) -> Permutation:
        perm = self
        for i in range(0, n - 1):
            perm = perm.get_composition(self)

        return perm

    def get_cycles(self) -> list[list]:
        not_used = []
        for i in range(0, self.length):
            not_used.append(i)

        cycles = []

        while len(not_used) != 0:
            start = not_used[0]
            temp = self.elements[start] - 1

            cycle = [start + 1]
            not_used.remove(start)

            if start != temp:
                cycle.append(temp + 1)
                not_used.remove(temp)

            while start != temp:
                temp = self.elements[temp] - 1

                if start != temp:
                    cycle.append(temp + 1)
                    not_used.remove(temp)

            cycles.append(cycle)

        return cycles

    def get_neural_degree(self) -> int:
        cycles = self.get_cycles()

        cycles_length = []
        for cycle in cycles:
            cycles_length.append(len(cycle))

        if cycles_length == 1:
            return cycles_length[0]

        result = lcm.calculate_lcm(cycles_length[0], cycles_length[1])

        if cycles_length == 2:
            return result

        for i in range(2, len(cycles_length) - 1):
            result = lcm.calculate_lcm(result, cycles_length[i])

        return result
