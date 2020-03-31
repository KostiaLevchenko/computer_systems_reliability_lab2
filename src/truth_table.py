def truth_table(n):
    if n < 1:
        return [[]]
    subtable = truth_table(n - 1)
    return [row + [v] for row in subtable for v in [0, 1]]
