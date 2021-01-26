#!/usr/bin/python

input = [["S", "E", "N", "D"], ["M", "O", "R", "E"]]
sum = ["M", "O", "N", "E", "Y"]

def populateSolutions(inputArray, solutions):
    for letter in inputArray:
        solutions[letter] = 'null'

def solveNode(index, solutions, carryForward):
    return 'unsolvable'
    #return {'S': 'null', 'E': 'null', 'N': 'null', 'D': 'null', 'M': 'null', 'O': 'null', 'R': 'null', 'Y': 'null'}
    #return solutions

def solveProblem(input, sum):
    solutions = dict()

    populateSolutions(input[0], solutions)
    populateSolutions(input[1], solutions)
    populateSolutions(sum, solutions)

    noCarrySolutions = solutions.copy()
    noCarry = solveNode(0, noCarrySolutions, 0)
    if (noCarry != 'unsolvable'):
        print ("Solution Found!")
        print (noCarry)
    
    withCarrySolutions = solutions.copy()
    withCarry = solveNode(0, withCarrySolutions, 1)
    if (withCarry != 'unsolvable'):
        print ("Solution Found!")
        print(withCarry)

    if ((noCarry == 'unsolvable') and (withCarry == 'unsolvable')):
        print ("ERROR:  No solution found...")
        exit(1)

solveProblem(input, sum)