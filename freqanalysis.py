#!/usr/bin/env python3

# Frequency analysis library
# by moosd 2015

import common

def freqtable(text):
    text = text.lower()
    freq = [0] * 26
    for c in text:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            freq[ord(c) - ord('a')] += 1
    return freq

def simpleshift(text):
    # simple version:
    # get highest frequency letter and assume it is an e
    # return shift as an integer
    freq = freqtable(text)
    return (freq.index(max(freq)) - (ord('e') - ord('a')))

if __name__ == "__main__":
    text = common.argfiletext()
    print(freqtable(text))
