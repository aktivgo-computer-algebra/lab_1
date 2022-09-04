import permutation


# elements = [4, 2, 7, 6, 5, 8, 1, 3] -> ([1, 4, 6, 8, 3, 7], [2], [5])

def read_permutation(length: int) -> permutation.Permutation:
    print("input elements: ")

    elements = []
    for i in range(0, length):
        element = int(input())
        elements.append(element)

    return permutation.Permutation(length, elements)


if __name__ == '__main__':
    n = int(input("input permutations length: "))

    perm_1 = read_permutation(n)
    perm_2 = read_permutation(n)

    print("perm_1:", perm_1.elements)
    print("perm_2:", perm_2.elements)

    print("neutral perm of perm_1:", perm_1.get_neural_permutation().elements)
    print("neutral perm of perm_2:", perm_2.get_neural_permutation().elements)

    print("composition of perm_1 and perm_2:", perm_1.get_composition(perm_2).elements)
    print("composition of perm_2 and perm_1:", perm_2.get_composition(perm_1).elements)

    print("reverse permutation of perm_1:", perm_1.get_reverse_permutation().elements)
    print("reverse permutation of perm_2:", perm_2.get_reverse_permutation().elements)

    degree = int(input("input degree: "))

    print("permutation of", degree, "degree of perm_1:", perm_1.get_degree_permutation(degree).elements)
    print("permutation of", degree, "degree of perm_2:", perm_2.get_degree_permutation(degree).elements)

    print("cycles of perm_1:", perm_1.get_cycles())
    print("cycles of perm_2:", perm_2.get_cycles())

    print("neutral degree of perm_1:", perm_1.get_neural_degree())
    print("neutral degree of perm_2:", perm_2.get_neural_degree())
