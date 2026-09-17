# Checks if the differences are equal
def same_difference(diffs):
        # Iterates through differences and sees if they are equal
        same = True
        for j in range(0, len(diffs)-1):
                if diffs[j+1] != diffs[j]:
                        same = False
                        break
        return same
                        

# Calculates the difference between any 2 consecutve terms in a sequence
def finite_differences(sequence, degree=1):
        differences=[]
        # Iterates through sequence to find the difference
        for i in range(0, len(sequence)-1):
                difference = sequence[i+1] - sequence[i]
                differences.append(difference)

        # Checks if differences are equal
        if same_difference(differences):
                return differences, degree
        else:
                degree += 1
                return finite_differences(differences, degree)

# Sequence must have enough terms to reach a constant difference
seq1 = [1, 8, 27, 64, 125]        
print(finite_differences(seq1))
