#!/usr/bin/python

input = [["S", "E", "N", "D"], ["M", "O", "R", "E"]]
sum = ["M", "O", "N", "E", "Y"]

def populateSolutions(inputArray, solutions):
    for letter in inputArray:
        solutions[letter] = 'null'

def solveNode(index, solutions, carryForward):
    print("todo")

def solveProblem(input, sum):
    solutions = dict()

    populateSolutions(input[0], solutions)
    populateSolutions(input[1], solutions)
    populateSolutions(sum, solutions)

    print(solutions)

solveProblem(input, sum)