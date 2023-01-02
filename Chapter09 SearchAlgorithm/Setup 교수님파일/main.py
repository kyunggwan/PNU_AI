from problem import *
from optimizer import *

def main():
    # Select and create a Problem object
    p, pType = selectProblem()  # A specific problem and its type
    # Determine the search algorithm to be used
    alg = selectAlgorithm(pType)
    # Call the search algorithm
    alg.run(p)
    # Show the problem solved
    p.describe()
    # Show the algorithm settings
    alg.displaySetting()
    # Report results
    p.report()

def selectProblem():
    print("Select the problem type:")
    print("  1. Numerical Optimization")
    print("  2. TSP")
    pType = int(input("Enter the number: "))
    if pType == 1:      #
        p = Numeric()   # Create an empty problem instance
    elif pType == 2:    #
        p = Tsp()       #
    p.setVariables()    # Now 'p' is a specific problem instance
    return p, pType

def selectAlgorithm(pType):
    print()
    print("Select the search algorithm:")
    print("  1. Steepest-Ascent")
    print("  2. First-Choice")
    print("  3. Gradient Descent")
    while True:
        aType = int(input("Enter the number: "))
        if not invalid(pType, aType):
            break
    optimizers = { 1: 'SteepestAscent()',
                   2: 'FirstChoice()',
                   3: 'GradientDescent()' }
    alg = eval(optimizers[aType])     # Create the target algorithm
    alg.setVariables(pType)
    return alg

def invalid(pType, aType):
    if pType == 2 and aType == 3:
        print("You cannot choose Gradient Descent")
        print("   unless your want a function optimization.")
        return True
    else:
        return False

main()
