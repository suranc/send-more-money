#!/usr/bin/python

input = [["S", "E", "N", "D"], ["M", "O", "R", "E"]]
sum = ["M", "O", "N", "E", "Y"]

def populateSolutions(inputArray, solutions):
    for letter in inputArray:
        solutions[letter] = 'null'

def solveNode(index, solutions, carryForward):
    return 'unsolvable'

def solveProblem(input, sum):
    solutions = dict()

    populateSolutions(input[0], solutions)
    populateSolutions(input[1], solutions)
    populateSolutions(sum, solutions)

    noCarry = solveNode(0, solutions, 0)
    withCarry = solveNode(0, solutions, 1)
    if (noCarry != 'unsolvable'):
        print ("Solution Found!")
        print (noCarry)
    elif (withCarry != 'unsolvable'):
        print ("Solution Found!")
        print(withCarry)
    else:
        print ("ERROR:  No solution found...")
        exit(1)

solveProblem(input, sum)