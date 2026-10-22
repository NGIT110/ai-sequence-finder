from sequence_analyser import analyse
from genetic_ai import analyse_gp
 
 
# Tries the exact methods first, then the genetic programming
def solve(sequence):
 
    result = analyse(sequence)
    if result["solved"]:
        result["method"] = "exact"
        return result
 
    result = analyse_gp(sequence)
    result["method"] = "genetic"
    return result
 
 
# Reads a sequence typed by the user, returns None if it isn't valid
def read_sequence(text):
 
    numbers = []
 
    for piece in text.split(","):
        try:
            numbers.append(int(piece))
        except ValueError:
            return None
 
    return numbers
 
 
# Prints the result in a readable way
def show(result):
 
    if result["method"] == "exact":
        print("Method:    exact (" + result["kind"] + ")")
    else:
        print("Method:    genetic programming")
 
    if not result["solved"]:
        print("No exact rule found. This is the closest fit (total error " + str(result["error"]) + "), so treat it with caution.")
 
    print("Rule:      a(n) = " + result["rule"])
    print("Next term: " + str(result["next_term"]))
 
    if result["method"] == "genetic" and result["solved"]:
        print("Note: this rule fits every term you gave, but that does not prove it is the true rule.")
 
 
def main():
 
    print("Sequence solver. Type a sequence like 1, 4, 9, 16, 25 (blank line to quit).")
 
    while True:
 
        text = input("> ").strip()
 
        if text == "":
            break
 
        sequence = read_sequence(text)
 
        if sequence is None:
            print("Please enter whole numbers separated by commas.")
        elif len(sequence) < 3:
            print("Please enter at least 3 numbers.")
        else:
            show(solve(sequence))
 
 
if __name__ == "__main__":
    main()