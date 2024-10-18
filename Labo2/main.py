from resources import *
from super_functions import *

def testAllFunctions():
    #Task 1
    numbers_list = [3, 1, 4, 1, 5, 9, 2]
    mean, median = calculateMeanAndMedian(numbers_list)
    print(f"Mean: {mean}, Median: {median}")

    #Task 2
    numbers_tuple = (3, 1, 4, 1, 5, 9, 2)
    sorted_numbers = sortTuple(numbers_tuple)
    print(f"Sorted list: {sorted_numbers}")

    #Task 3
    matrix = [
        [1, None, 3],
        [4, 5, None],
        [None, None, 9]
    ]

    empty_fields = countEmptyFields(matrix)
    print(f"Number of empty fields: {empty_fields}")

    #Task 5
    text = "Hi there from laboratories number 2"
    print(f"Word count: {countWordsInText(text)}")
    print(f"Reversed text: {reverseWordsInText(text)}")
    print(f"Text with removed whitespaces: {removeWhiteSpaceInText(text)}")

    number = 12345
    print(f"Summary of digits: {calculateSumOfDigitsInNumber(number)}")
    print(f"Factorial of 6: {calculateFactorial(6)}")

testAllFunctions()