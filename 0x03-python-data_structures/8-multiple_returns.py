#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sentc_len = len(sentence)
    else:
        sentc_len = 0
    return (sentc_len, sentence if not sentence else sentence[:1])
