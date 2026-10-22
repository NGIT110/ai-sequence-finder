import random
from fractions import Fraction
from sequence_analyser import rule_as_text



# Global constants
operators = ["*", "-", "+"]
lam = 0.1
k = 10
mutation_rate = 0.05


# Completes operation
def operation(operator, left, right):

    if operator == "+":
         return left + right
    elif operator == "-":
         return left - right
    elif operator == "*":
         return left*right


# evaluates a tree
def evaluate(tree, n):

    # Checks if tree is tuple or base case integer
    if not isinstance(tree, tuple):
        if tree == "n":
            return n
        else:
            return tree 

    operator = tree[0]
    left = evaluate(tree[1], n)
    right = evaluate(tree[2], n)

    return(operation(operator, left, right))


# Returns a sequence
def sequence_from_tree(tree, length):

    seq = []

    for n in range(1, length+1):
        term = evaluate(tree, n)
        seq.append(term)

    return seq


# Finds error between the target sequence and the tree sequence
def error(tree, target):

    error_interval = 0
    sequence = sequence_from_tree(tree, len(target))

    for i in range(0, len(target)):
        error_interval += abs(target[i]-sequence[i])

    return error_interval


# Counts nodes in a tree 
def count_nodes(tree, nodes=0):

    # Base case if tree is a single number
    if not isinstance(tree, tuple):
        return 1

    
    for node in tree:
        if isinstance(node, tuple):
            nodes += count_nodes(node)
        else:
            nodes += 1

    return nodes


# Defines a fitness score
def fitness(tree, target, lam):
    return error(tree, target) + lam * count_nodes(tree)


# Creates a random tree
def random_tree(depth):
    if depth == 0:
        return random.choice(["n", 1, 2, 3])
    else:
        if random.random() < 0.2:
            return random.choice(["n", 1, 2, 3])
        else:
            operator = random.choice(operators)
            left, right = random_tree(depth-1), random_tree(depth-1)
            return (operator, left, right)


# Makes a population of trees
def make_population(size, depth):

    population = []

    for _ in range(size):
        tree = random_tree(depth)
        population.append(tree)

    return population


# Returns the best tree out of a population
def tournament(population, target, lam, k): 
    # k is the number of trees that compete
    # lam is for the fitness function
    
    contestants = random.sample(population, k)

    best_tree = ()
    best_score = float("inf") # Very large number

    for contestant in contestants:

        score = fitness(contestant, target, lam)

        if score < best_score:

            best_score = score
            best_tree = contestant

    return best_tree, best_score


# Returns a mutated tree
def mutate(tree, mutation_rate):

    if random.random() < mutation_rate:
        return random_tree(2)
    
    else:

        if isinstance(tree, tuple):

            new_left = mutate(tree[1], mutation_rate)
            new_right = mutate(tree[2], mutation_rate)
            return (tree[0], new_left, new_right)
        
        else:
            return tree


# Returns all subtrees within a tree
def all_subtrees(tree):

    if not isinstance(tree, tuple):
        return [tree]
    
    else:

        left = all_subtrees(tree[1])
        right = all_subtrees(tree[2])

    return [tree] + left + right 


# Retruns the crossover between 2 trees
def crossover(parent_a, parent_b, crossover_rate=None, subtree_from_b=None):

    if crossover_rate is None:
        crossover_rate = 1/count_nodes(parent_a)

    if subtree_from_b is None:
        subtree_from_b = random.choice(all_subtrees(parent_b))

    if random.random() < crossover_rate:
        return subtree_from_b

    else:

        if isinstance(parent_a, tuple):

            new_left = crossover(parent_a[1], parent_b, crossover_rate, subtree_from_b)
            new_right = crossover(parent_a[2], parent_b, crossover_rate, subtree_from_b)

            return (parent_a[0], new_left, new_right)
        
        else:
            return parent_a


# Evolves the population
def evolve(target, pop_size, depth, generations, lam, k, mutation_rate, max_nodes=40):

    pop = make_population(pop_size, depth)

    for gen in range(generations+1):

        best_tree = ()
        best_score = float("inf")

        for tree in pop:

            fitness_score = fitness(tree, target, lam)

            if best_score > fitness_score:

                best_tree = tree
                best_score = fitness_score

        if error(best_tree, target) == 0:
            return best_tree, gen, True

        if gen == generations:
            break

        new_pop = [best_tree]

        while len(new_pop) < pop_size:

            parent_a = (tournament(pop, target, lam, k))[0]
            parent_b = (tournament(pop, target, lam, k))[0]

            child = crossover(parent_a, parent_b)
            mutated_child = mutate(child, mutation_rate)

            if count_nodes(mutated_child) <= max_nodes:
                new_pop.append(mutated_child)

        pop = new_pop

    return best_tree, generations, False


# Simplifies the tree
def simplify(tree):

    if not isinstance(tree, tuple):
        return tree

    else:

        op = tree[0]
        left = simplify(tree[1])
        right = simplify(tree[2])

        if is_number(left) and is_number(right):
            return operation(op, left, right)
        
        else:  

            if op == "+":

                if left == 0 :
                    return right

                if right == 0:
                    return left

            if op == "-":

                if right == 0:
                    return left

                if left == right:
                    return 0

            if op == "*":

                if left == 0 or right == 0:
                    return 0

                if left == 1:
                    return right

                if right == 1:
                    return left
            

            return (op, left, right)


# Helper check for simplify
def is_number(x):
    return not isinstance(x, tuple) and x != "n"


# Test function for simplify
def same_values(tree_a, tree_b):

    for n in range(1, 21):

        if evaluate(tree_a, n) !=  evaluate(tree_b, n):
            return False

    return True


# Adds to polynomials via their coefficients
def poly_add(a, b):

    size = max(len(a), len(b))
    result = []

    for i in range(0, size):
        total = 0
        if i < len(a):
            total += a[i]
        if i < len(b):
            total += b[i]
        result.append(total)

    return result


# Subtracts polynomial b from a
def poly_sub(a, b):

    size = max(len(a), len(b))
    result = []

    for i in range(0, size):
        total = 0
        if i < len(a):
            total = total + a[i]
        if i < len(b):
            total = total - b[i]
        result.append(total)

    return result


# Multiplies two polynomials
def poly_mul(a, b):
    result = [Fraction(0)] * (len(a) + len(b) - 1)

    for i in range(0, len(a)):
        for j in range(0, len(b)):
            result[i + j] = result[i + j] + a[i] * b[j]

    return result


# Checks that a tree only uses + - * numbers and n
def is_polynomial_tree(tree):
    if not isinstance(tree, tuple):
        return True

    if tree[0] not in ["+", "-", "*"]:
        return False

    return is_polynomial_tree(tree[1]) and is_polynomial_tree(tree[2])


# Turns a polynomial tree into a list of coefficients
def tree_to_poly(tree):

    if not isinstance(tree, tuple):
        if tree == "n":
            return [Fraction(0), Fraction(1)]
        else:
            return [Fraction(tree)]

    left = tree_to_poly(tree[1])
    right = tree_to_poly(tree[2])

    if tree[0] == "+":
        return poly_add(left, right)
    elif tree[0] == "-":
        return poly_sub(left, right)
    else:
        return poly_mul(left, right)


# Works out the value of a coefficient list at a given n (used for testing)
def poly_value(poly, n):
    total = 0
    for i in range(0, len(poly)):
        total = total + poly[i] * n ** i
    return total


# Writes any tree as text, with brackets round every operator
def tree_to_text(tree):
    if not isinstance(tree, tuple):
        return str(tree)

    left = tree_to_text(tree[1])
    right = tree_to_text(tree[2])
    return "(" + left + " " + tree[0] + " " + right + ")"


# Gives the simplest form of a tree as text
def simplest_form(tree):
    tree = simplify(tree)

    if is_polynomial_tree(tree):
        return rule_as_text(tree_to_poly(tree))
    else:
        return tree_to_text(tree)

    
# Runs the genetic programming and returns the same kind of dictionary as the analyser
def analyse_gp(sequence, attempts=3):

    lam = 0.1
    closest_tree = None
    closest_score = float("inf")

    for attempt in range(0, attempts):

        tree, gen, solved = evolve(sequence, 200, 3, 50, lam, 5, 0.1)

        if solved:
            return {"solved": True, "kind": "genetic",
                    "rule": simplest_form(tree),
                    "next_term": evaluate(tree, len(sequence) + 1)}

        # Not solved, so keep it if it is the closest so far
        score = fitness(tree, sequence, lam)
        if score < closest_score:
            closest_tree = tree
            closest_score = score

    # Returns closest rule
    return {"solved": False, "kind": "genetic",
            "rule": simplest_form(closest_tree),
            "next_term": evaluate(closest_tree, len(sequence) + 1),
            "error": error(closest_tree, sequence)}


if __name__ == "__main__":
    """
    t = ("-", ("+", ("*", "n", "n"), "n"), 2)
    tree_a = ("*", "n", "n")
    tree_b = ("-", "n", 3)
    target = [1, 8, 27, 64, 125]


    print(evaluate(t, 5))
    print(sequence_from_tree(t, 5))

    print(error(t, target))
    print(count_nodes(t))
    print(fitness(t, target, 0.5))

    t1 = ("+", ("*", "n", "n"), ("*", ("-", "n", "n"), "n"))
    print(fitness(t1, target, 0.5))

    print(random_tree(2))


    depth = 3
    for _ in range(10):
        tree = random_tree(depth)
        print(tree)
        print(evaluate(tree, 2))
        print(count_nodes(tree))


    print(make_population(10, 3))


    pop = make_population(200, 3)
    best_t, best_s = tournament(pop, [1, 4, 9, 16, 25], 0.1, 100)
    print(best_t, best_s)


    print(mutate(t, 0.2))


    print(all_subtrees(tree_b))


    print(crossover(tree_a, tree_b))

    print(evolve(target,  100, 3, 3, lam, k, mutation_rate))


    tree, gen, solved = evolve(target, 200, 3, 30, 0.1, 5, 0.1)
    print(tree, gen, solved)
    """

    t = ("*", ("+", "n", 1), ("+", "n", 1))
    print(simplest_form(t))                     # should print n^2 + 2n + 1
    poly = tree_to_poly(t)
    print(poly_value(poly, 3), evaluate(t, 3))  # both should print 16