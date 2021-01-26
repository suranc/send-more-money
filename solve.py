#!/usr/bin/python

input = [["S", "E", "N", "D"], ["M", "O", "R", "E"]]
sum = ["M", "O", "N", "E", "Y"]

solutions = dict()

def populateSolutions(inputArray, solutions):
    for letter in inputArray:
        solutions[letter] = 'null'

populateSolutions(input[0], solutions)
populateSolutions(input[1], solutions)
populateSolutions(sum, solutions)

