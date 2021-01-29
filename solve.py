#!/usr/bin/python
import math

input = [[" ", "S", "E", "N", "D"], [" ", "M", "O", "R", "E"]]
sum = ["M", "O", "N", "E", "Y"]

# Adds an entry to the solutions dictionary for each unique letter
def populateSolutions(inputArray, solutions):
    for letter in inputArray:
        if (letter != ' '):
            solutions[letter] = None

# Populate test cases for each digit.
# Returns a 2d array with each element being an array of possibilities for that digit. 
def populateTestCases(letter1, letter2, letter3, solutions):
    unsolvedNumbers = {0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
    result = []
    letters = [letter1, letter2, letter3]

    # Create a list of numbers that aren't solved, by reversing the solutions dictionary and ignoring null values
    for letter in list(solutions.keys()):
        if (solutions[letter] != None):
            unsolvedNumbers[solutions[letter]] = 1
    unsolvedNumbersArray = []
    for number in list(unsolvedNumbers.keys()):
        if (unsolvedNumbers[number] == None):
            unsolvedNumbersArray.append(number)
    
    # For each letter in test cases, set test case list to just the solved number if it's solved in solutions.
    # Otherwise, set letter test cases to entire entire set of possibilities from unsolvedNumbersArray list
    for index in range(0,len(letters)):
        if (solutions[letters[index]] != None):
            result.append([solutions[letters[index]]])
        else:
            result.append(unsolvedNumbersArray)

    return result

# Change array of letters into numbers by using solutions dictionary
def lookupNumbers(letters, solutions):
    # Strip off any leading spaces from input letters array
    if (letters[0] == ' '):
        letters = letters[1:]

    # Fill out result by looping through input array left to right, and adding together each value*place (6*1000 + 5*100, etc)
    result = 0
    for place in range(0, len(letters)):
        result = result + solutions[letters[place]]*math.pow(10,len(letters) - place)

    return result

# Solve each "node" with a node being a column of digits in the equation
def solveNode(index, input, sum, solutions, carry, carryForward):
    # Check base case, see if final solution is valid and return solution if it is
    if (index == len(input[0])):
        if (lookupNumbers(input[0],solutions) + lookupNumbers(input[1],solutions) == lookupNumbers(sum,solutions)):
            return solutions

    # If solution at index of sum is null, and space is in input, letter must be 1.  Since carry forward at front can't be zero, and addition can only carry forward one
    elif ( (solutions[sum[index]] == None) and (input[0][index] == ' ') ):
        # Create branch solutions to carry forward
        branchSolutions = solutions.copy()
        branchSolutions[sum[index]] = 1

        # Solve with and without carry, return first result if solvable, and if not, whatever second result is (unsolvable still, or a valid solution)
        result = solveNode(index+1, input, sum, branchSolutions, 0, 1)
        if (result != 'unsolvable'):
            return result

        # No match without carry, try to solve with carry
        branchSolutionsCarry = solutions.copy()
        branchSolutionsCarry[sum[index]] = 1
        carryResult = solveNode(index+1, input, sum, branchSolutionsCarry, 1, 1)
        if (carryResult != 'unsolvable'):
            return (carryResult)
    else:
        # Get test cases from three digits to solve
        testCases = populateTestCases(input[0][index], input[1][index], sum[index], solutions)

        # Loop through each layer of the test cases, testing each permutation
        for input1 in testCases[0]:
            for input2 in testCases[1]:
                for sum3 in testCases[2]:
                    # Create branch solutions to carry forward
                    branchSolutions = solutions.copy()

                    # Skip cases where candidate is already found (shouldn't happen, FIX-skip for now) or duplicate candidates are hit
                    if ( (input1 == input2) or (input1 == sum3) or (input2 == sum3) ):
                        next

                    # If carryFoward = 1, sum must be >= 10, if 0, must be < 10
                    if (input1 + input2 + carry == (sum3 + 10*carryForward)):
                        # Populate these test solutions into branchSolutions
                        branchSolutions[input[0][index]] = input1
                        branchSolutions[input[1][index]] = input2
                        branchSolutions[sum[index]] = sum3
                        
                        # Solve with and without carry, return first result if solvable, and if not, whatever second result is (unsolvable still, or a valid solution)
                        result = solveNode(index+1, input, sum, branchSolutions, 0, carry)
                        if (result != 'unsolvable'):
                            return result

                        # No match without carry, try to solve with carry
                        branchSolutionsCarry = solutions.copy()
                        branchSolutionsCarry[input[0][index]] = input1
                        branchSolutionsCarry[input[1][index]] = input2
                        branchSolutionsCarry[sum[index]] = sum3
                        carryResult = solveNode(index+1, input, sum, branchSolutionsCarry, 1, carry)
                        if (carryResult != 'unsolvable'):
                            return (carryResult)

    # If nothing matches, current solution path is bust.  Return unsolvable
    return "unsolvable"

def solveProblem(input, sum):
    solutions = dict()

    populateSolutions(input[0], solutions)
    populateSolutions(input[1], solutions)
    populateSolutions(sum, solutions)
    solutionsCarry = solutions.copy()

    # Solve for first digit without carry
    solution = solveNode(0, input, sum, solutions, 0, 0)
    if (solution != 'unsolvable'):
        print ("Solution Found!")
        print (solution)
        exit(0)

    # No match without carry, try to with carry
    solution = solveNode(0, input, sum, solutionsCarry, 1, 0)
    if (solution != 'unsolvable'):
        print ("Solution Found!")
        print (solution)
        exit(0)

    print ("ERROR:  No solution found...")
    exit (1)

solveProblem(input, sum)