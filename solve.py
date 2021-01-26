#!/usr/bin/python

input = [[" ", "S", "E", "N", "D"], [" ", "M", "O", "R", "E"]]
sum = ["M", "O", "N", "E", "Y"]

def populateSolutions(inputArray, solutions):
    for letter in inputArray:
        if (letter != ' '):
            solutions[letter] = 'null'

def solveNode(index, input, sum, solutions, carry, carryForward):  #### Add carry, changing carryForward to if it pushes forward a 1 or not, and then have carry, whether or not it takes a carry?
    # Check base case - TODO Check for solution before we hit this point?
    if (index == len(input[0])):
        return solutions # Check if all letters != null, otherwise return unsolvable?
    # If solution at index of sum is null, and space is in input, letter must be 1.  Since carry forward at front can't be zero, and addition can only carry forward one
    elif ( (solutions[sum[index]] == 'null') and (input[0] == ' ') ):
        solutions[sum[index]] = 1
    else:
        # Make set to iterate through
        # digit # = unsolve input1, input2, sum1
        # possibilities = numbers not found in solutions
        return "solutions" # Solve problem for each carry possibility
    
    # noCarrySolutions = solutions.copy()
    # noCarry = solveNode(0, input, sum, noCarrySolutions, 0)
    # if (noCarry != 'unsolvable'):
    #     print ("Solution Found!")
    #     print (noCarry)
    
    # withCarrySolutions = solutions.copy()
    # withCarry = solveNode(0, input, sum, withCarrySolutions, 1)
    # if (withCarry != 'unsolvable'):
    #     print ("Solution Found!")
    #     print(withCarry)

    return 'unsolvable'

def solveProblem(input, sum):
    solutions = dict()

    populateSolutions(input[0], solutions)
    populateSolutions(input[1], solutions)
    populateSolutions(sum, solutions)

    solution = solveNode(0, input, sum, solutions, 1, 0)
    if (solution != 'unsolvable'):
        print ("Solution Found!")
        print(solution)
    else:
        print ("ERROR:  No solution found...")
        exit(1)

solveProblem(input, sum)