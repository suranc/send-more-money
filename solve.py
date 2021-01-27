#!/usr/bin/python

input = [[" ", "S", "E", "N", "D"], [" ", "M", "O", "R", "E"]]
sum = ["M", "O", "N", "E", "Y"]

def populateSolutions(inputArray, solutions):
    for letter in inputArray:
        if (letter != ' '):
            solutions[letter] = 'null'

def populateTestCases(letter1, letter2, letter3, solutions):
    unsolvedNumbers = {'0': '0', '1': '0', '2': '0', '3': '0', '4': '0', '5': '0', '6': '0', '7': '0', '8': '0', '9': '0'}
    #unsolvedNumbers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    result = []
    letters = [letter1, letter2, letter3]

    for letter in list(solutions.keys()):
        if (solutions[letter] != 'null'):
            unsolvedNumbers[solutions[letter]] = 1

    unsolvedNumbersArray = []
    for number in list(unsolvedNumbers.keys()):
        if (unsolvedNumbers[number] == '0'):
            unsolvedNumbersArray.append(number)
    
    for index in range(0,len(letters)):
        # Set test case to solved number if it's solved in solutions.  Otherwise set to entire set of possibilities from unsolvedNumbers
        if (solutions[letters[index]] != 'null'):
            result.append([solutions[letters[index]]])
        else:
            result.append(unsolvedNumbersArray)

    return result

def solveNode(index, input, sum, solutions, carry, carryForward):  #### Add carry, changing carryForward to if it pushes forward a 1 or not, and then have carry, whether or not it takes a carry?
    # Create branch solutions to carry forward
    branchSolutions = solutions.copy()
    branchSolutionsCarry = solutions.copy()

    # Check base case - TODO Check for solution before we hit this point?
    if (index == len(input[0])):
        print("all your base")
        return solutions # Check if all letters != null, otherwise return unsolvable?
    # If solution at index of sum is null, and space is in input, letter must be 1.  Since carry forward at front can't be zero, and addition can only carry forward one
    elif ( (solutions[sum[index]] == 'null') and (input[0][index] == ' ') ):
        branchSolutions[sum[index]] = '1'
        branchSolutionsCarry[sum[index]] = '1'
        
        print ("Solved first letter")

        # Solve with and without carry, return first result if solvable, and if not, whatever second result is (unsolvable still, or a valid solution)
        result = solveNode(index+1, input, sum, branchSolutions, 0, 1)
        if (result != 'unsolvable'):
            return result
        else:
            return (solveNode(index+1, input, sum, branchSolutionsCarry, 1, 1))
    else:
        # Get test cases from three digits, no carry first
        testCases = populateTestCases(input[0][index], input[1][index], sum[index], branchSolutions)
        print (testCases)
        # Loop through each layer of the test cases, testing each permutation
        for input1 in testCases[0]:
            for input2 in testCases[1]:
                for sum3 in testCases[2]:
                    # Skip cases where candidate is already found (shouldn't happen, FIX-skip for now) or duplicate candidates are hit
                    if ( (input1 == input2) or (input1 == sum3) or (input1 == sum3) or (input2 == sum3) ):
                        print("skipping...")
                        print ("carryForward: " + str(carryForward) + " input1: " + input1 + " - input2: " + input2 + " - carry: " + str(carry) + " - sum3: " + str(int(sum3) + 10*carryForward))
                        next

                    #if (carryForward == 1): # If carryFoward = 1, sum must be >= 10, if 0, must be < 10
                    if (int(input1) + int(input2) + int(carry) == int(sum3) + 10*carryForward):
                        # Populate these test solutions into branchSolutions
                        branchSolutions[input[0][index]] = input1
                        branchSolutions[input[1][index]] = input2
                        branchSolutions[sum[index]] = sum3
                        branchSolutionsCarry[input[0][index]] = input1
                        branchSolutionsCarry[input[1][index]] = input2
                        branchSolutionsCarry[sum[index]] = sum3
                        print ("carryForward: " + str(carryForward) + " input1: " + input1 + " - input2: " + input2 + " - carry: " + str(carry) + " - sum3: " + str(int(sum3) + 10*carryForward))
                        # Solve with and without carry, return first result if solvable, and if not, whatever second result is (unsolvable still, or a valid solution)
                        result = solveNode(index+1, input, sum, branchSolutions, 0, carry)
                        print (index+1, input, sum, branchSolutions, 0, carry)
                        if (result != 'unsolvable'):
                            print ("not unsolve")
                            print (result)
                            return result
                        else:
                            print("returning from carry")
                            return (solveNode(index+1, input, sum, branchSolutionsCarry, 1, carry))
    return "unsolvable"

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