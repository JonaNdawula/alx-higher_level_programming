#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_length = len(sentence)
    if sentence == "":
        return (0, None)
    return (sentence_length, sentence[0])
