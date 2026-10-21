from math import comb, factorial
from fractions import Fraction


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

        # A level needs at least 2 numbers, or we can't trust it
        if len(current) < 2:
            return None


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


# Multiplies a polynomial by (n - c)
def multiply_by_n_minus(poly, c):
    new_poly = [0] * (len(poly) + 1)
    for i in range(0, len(poly)):
        new_poly[i + 1] = new_poly[i + 1] + poly[i]
        new_poly[i] = new_poly[i] - c * poly[i]
    return new_poly


# Turns the first values into ordinary coefficients of n
# Uses C(n-1, k) = (n-1)(n-2)...(n-k) / k!
def to_coefficients(first_values):
    total = [Fraction(0)] * len(first_values)
    poly = [Fraction(1)]

    for k in range(0, len(first_values)):
        if k > 0:
            poly = multiply_by_n_minus(poly, k)
        for i in range(0, len(poly)):
            total[i] = total[i] + first_values[k] * poly[i] / factorial(k) # Division occurs here as the next iteration needs poly to be undivided

    return total


# Writes one term like 3n^2 (c is always positive here)
def term_text(c, power):
    if c.denominator != 1:
        number = "(" + str(c) + ")"
    else:
        number = str(c)

    if power == 0:
        return number

    if power == 1:
        variable = "n"
    else:
        variable = "n^" + str(power)

    if c == 1:
        return variable
    return number + variable


# Writes the whole rule as text, highest power first
def rule_as_text(coefficients):
    text = ""

    for power in range(len(coefficients) - 1, -1, -1):
        c = coefficients[power]

        if c == 0:
            continue

        if c < 0:
            sign = " - "
            c = -c
        else:
            sign = " + "

        piece = term_text(c, power)

        if text == "":
            if sign == " - ":
                text = "-" + piece
            else:
                text = piece
        else:
            text = text + sign + piece

    if text == "":
        text = "0"

    return text


# Tries to find a polynomial rule, and returns everything in one dictionary
def analyse_polynomial(sequence):
    result = finite_differences(sequence)

    if result is None:
        return {"solved": False}

    first_values, degree = result
    coefficients = to_coefficients(first_values)

    return {
        "solved": True,
        "kind": "polynomial",
        "degree": degree,
        "rule": rule_as_text(coefficients),
        "next_term": nth_term(first_values, len(sequence) + 1),
    }



# Tries to find a geometric rule: each term is the one before times a fixed ratio
def analyse_geometric(sequence):

    if len(sequence) < 3:
        return {"solved": False}

    # A zero would mean dividing by zero, so skip these
    for term in sequence:
        if term == 0:
            return {"solved": False}

    ratios = []
    for i in range(0, len(sequence) - 1):
        ratio = Fraction(sequence[i + 1], sequence[i])
        ratios.append(ratio)

    if not same_difference(ratios):
        return {"solved": False}

    first = sequence[0]
    ratio = ratios[0]

    next_term = first * ratio ** len(sequence)
    if next_term.denominator == 1:
        next_term = int(next_term)

    return {
        "solved": True,
        "kind": "geometric",
        "ratio": str(ratio),
        "rule": geometric_rule_text(first, ratio),
        "next_term": next_term,
    }


# Writes the rule as text, like 2 * 3^(n-1)
def geometric_rule_text(first, ratio):

    if ratio.denominator != 1 or ratio < 0:
        ratio_text = "(" + str(ratio) + ")"
    else:
        ratio_text = str(ratio)

    if first == ratio:
        return ratio_text + "^n"

    if first == 1:
        return ratio_text + "^(n-1)"

    return str(first) + " * " + ratio_text + "^(n-1)"


# The function main.py will call: tries each exact method in order
def analyse(sequence):

    result = analyse_polynomial(sequence)
    if result["solved"]:
        return result

    result = analyse_geometric(sequence)
    if result["solved"]:
        return result

    return {"solved": False}


if __name__ == "__main__":
    tests = [
        [1, 4, 9, 16, 25],
        [10, 7, 4, 1, -2],
        [5, 5, 5, 5],
        [2, 6, 18, 54],
        [3, 9, 27, 81],
        [1, 2, 4, 8, 16],
        [16, 8, 4, 2],
        [1, -2, 4, -8],
        [2, 6],
        [3, 0, 0, 0],
        [1, 8, 27, 64, 126],
        [1, 1, 2, 3, 5, 8, 13],
    ]
    for seq in tests:
        print(seq, "->", analyse(seq))

