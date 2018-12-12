#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    else:
        a = len(sentence)
        b = sentence[0]
    return (a, b,)
