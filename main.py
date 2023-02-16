# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i+1))
            #pass

        elif next in ")]}":

            if len(opening_brackets_stack)==0:
            or not are_matching(opening_brackets_stack[-1].char,next_char):
             return i+1                             
            opening_brackets_stack.pop()
            if len(opening_brackets_stack) > 0:
             return opening_brackets_stack[0].position
            else: 
                return "Success"
            #pass


def main():
    ievade = input("Enter I for input or F for files: ")
    if ievade.lower() == "i":
        text = input("Enter text: ")
        result = find_mismatch(text)
        print(result)
    elif ievade.lower() == "f":
        filename = input("Enter file name: ")
        with open(filename, "r") as f:
            text = f.read().strip()
            result = find_mismatch(text)
            print(result)

if __name__ == "__main__":
    main()