#!/usr/bin/python3


def multiple_returns(sentence):
    return (len(sentence), None) if sentence == '' else (len(
            sentence), sentence[0])
