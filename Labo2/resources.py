def calculateMeanAndMedian(numbers : list[int, float]):
    if not numbers:
        return "Error. List is empty"

    numberSorted = sorted(numbers)

    mean = sum(numbers) / len(numbers)

    listLength = len(numbers)
    mid = listLength // 2

    if listLength % 2 == 0:
        median = (numberSorted[mid-1] + numberSorted[mid]) / 2
    else :
        median = numberSorted[mid]

    return mean, median

def sortTuple(numbers: tuple[int, ...]) -> list[int]:
    sortedTuple = sorted(numbers)

    return sortedTuple

def countEmptyFields(matrix: list[list[int]]) -> int:
    emptyCount = 0

    for row in matrix:
        for element in row:
            if element is None:
                emptyCount += 1

    return emptyCount