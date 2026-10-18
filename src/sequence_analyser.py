from math import comb


# Checks if every number in a list is the same
def same_difference(diffs):
    same = True
    for j in range(0, len(diffs) - 1):
        if diffs[j + 1] != diffs[j]:
            same = False
            break
    return same


# Finds the first value of every difference level, and the degree
def finite_differences(sequence):
    first_values = []
    current = sequence

    while True:
        # Save the first number of this level
        first_values.append(current[0])

        # If this level is all the same number, we can stop
        if same_difference(current):
            break

        # Otherwise work out the next level of differences
        differences = []
        for i in range(0, len(current) - 1):
            difference = current[i + 1] - current[i]
            differences.append(difference)
        current = differences

    # The degree is the number of levels we went down
    degree = len(first_values) - 1
    return first_values, degree


# Finds the nth term using the first values (Newton's forward difference formula)
def nth_term(first_values, n):
    total = 0
    for k in range(0, len(first_values)):
        total = total + first_values[k] * comb(n - 1, k)
    return total



seq = [1, 8, 27, 64, 125]
values, degree = finite_differences(seq)
print(values, degree)        
print(nth_term(values, 6))   
