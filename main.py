# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
            #pass

        if next in ")]}":
           if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
            return i+1
           opening_brackets_stack.pop()
        if opening_brackets_stack:
          return opening_brackets_stack[0].position
        return "Success"
          
       


def main():
    ievade = input("Enter I for input or F for files: ")
    if ievade.lower() == "i":
        text = input("Enter text: ")
        result = find_mismatch(text)
        print(result)
    elif ievade.lower() == "f":
        file = input("Enter file name: ")
        with open(file, "r") as f:
            text = f.read().strip()
            result = find_mismatch(text)
            print(result)

if __name__ == "__main__":
    main()