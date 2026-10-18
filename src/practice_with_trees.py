
# Complete operation
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
    left = evaluate(tree[1])
    right = evaluate(tree[2])


    return(operation(operator, left, right))


t = ("*", ("*", "n", "n"), 4)
print(evaluate(t, 4))
    