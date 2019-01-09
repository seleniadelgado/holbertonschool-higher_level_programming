#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.lstrip()
    i = 0
    while i < (len(text)):
        print(text[i], end="")
        if text[i] == "?" or text[i] == "." or text[i] == ":":
            print("\n")
            while i < len(text) - 1 and text[i + 1] == " ":
                i += 1
        i += 1
