import random

operators = ["*", "-", "+"]

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


"""
t = ("*", "n", "n")
target = [1, 4, 9, 16, 27]


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
"""