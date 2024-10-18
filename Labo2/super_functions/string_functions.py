def countWordsInText(text: str) -> int:
    return len(text.split())

def reverseWordsInText(text: str) -> str:
    splitedWords = text.split()

    return ' '.join(reversed(splitedWords))

def removeWhiteSpaceInText(text: str) -> str:
    return text.replace(' ', '')