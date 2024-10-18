def calculateSumOfDigitsInNumber(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))

def calculateFactorial(number: int) -> int:
    if number < 0:
        return "Error"

    end = 1
    for i in range(2, number + 1):
        end = end * i

    return end