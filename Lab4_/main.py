from typing import List, Any


def sortByNumbersCount(nums: List[int]) -> None:
    """Organizes a list of integers by the count of digits in each number,
    displaying the one with the most and fewest digits."""
    sortedNums = sorted(nums, key=lambda l: len(str(abs(l))))

    maxDigitNum = max(sortedNums, key=lambda l: len(str(abs(l))))
    minDigitNum = min(sortedNums, key=lambda l: len(str(abs(l))))

    print("Most digits: ", maxDigitNum)
    print("Least digits: ", minDigitNum)

def firstCapitalBigLastCharIsDot(text: List[str]) -> List[str]:
    """Reformats each string to begin with an uppercase letter and ensures
    it ends with a period."""
    return list(map(lambda t: t.capitalize().rstrip('.') + '.', text))

def processingStringsFloatsInts(*args):
    """Handles arguments by type: computes the average for numeric inputs,
    finds the median length of strings, or signals an error for mixed types."""
    if all(isinstance(arg, (int,float)) for arg in args):
        return sum(args) / len(args) if args else 0

    elif all(isinstance(arg, str) for arg in args):
        lengths = sorted(len(arg) for arg in args)
        allLengths = len(lengths)
        half = allLengths // 2
        if allLengths % 2 == 1:
            return lengths[half]
        else:
            return (lengths[half-1] + lengths[half]) / 2
    else:
        return "Something went wrong. Args must be numbers or strings"

def advancedProcessingStringsFloatsInts(*args: Any, **kwargs: Any) -> None:
    """Differentiates handling based on argument type: lists positional arguments,
    writes named arguments to a file, or combines both in a dictionary."""
    if args and not kwargs:
        print("Created list:", "\t".join(str(arg) for arg in args))

    elif kwargs and not args:
        with open("Lab4_Task4.txt", "w") as file:
            for key, value in kwargs.items():
                file.write(f"{key} -> {value}\n")
        print("Saved to text file")
    elif args and kwargs:
        differentType = {f"arg{i+1}": arg for i, arg in enumerate(args)}
        differentType.update(kwargs)
        print("Mixed args as dict: ",differentType)


nums = [1234, 50, 6, 123456, 764, 8753, 17]
text = ["advanced python", "testing function", "lambda usage", "last test"]
#Task 1
sortByNumbersCount(nums)

#Task 2
formatedText = firstCapitalBigLastCharIsDot(text)
print(formatedText)

#Task 3
print(processingStringsFloatsInts(8,15,12,76,23,1,6))
print(processingStringsFloatsInts("advanced","python","class"))
print(processingStringsFloatsInts(1,"python",1.7))

#Task 4
advancedProcessingStringsFloatsInts(1,2,3,4)
advancedProcessingStringsFloatsInts(name="Radek", age=24, classes="Advanced python")
advancedProcessingStringsFloatsInts(1,2, name="Sample name", age=42)