# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i+1)
            #pass

        if next in ")]}":

            if len(opening_brackets_stack)==0 
            or not are_matching(opening_brackets_stack[-1].char,next_char):
            return i+1                             
            opening_brackets_stack.pop()
            if len(opening_brackets_stack) > 0:
            return opening_brackets_stack[0].position
            else: 
                return "Success"
            #pass


def main():
    ievade = input("Input-I, File-F")
    if ievade.lower() == "f":                                                                           
    text = input("")                                      
    mismatch = find_mismatch(text)