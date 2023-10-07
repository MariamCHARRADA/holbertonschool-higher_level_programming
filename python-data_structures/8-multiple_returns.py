#!/usr/bin/python3
def multiple_returns(sentence):
    res = []
    res.append(len(sentence))
    if len(sentence) == 0:
        first = 'None'
    else:
        first = sentence[0]
    res.append(first)
    return tuple(res)
