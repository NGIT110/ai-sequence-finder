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






t = ("*", "n", "n")
target = [1, 4, 9, 16, 27]

print(evaluate(t, 5))
print(sequence_from_tree(t, 5))

print(error(t, target))
print(count_nodes(t))
print(fitness(t, target, 0.5))

t1 = ("+", ("*", "n", "n"), ("*", ("-", "n", "n"), "n"))
print(fitness(t1, target, 0.5))

