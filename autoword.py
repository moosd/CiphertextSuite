#!/usr/bin/env python3

import sys, common

max_word_len = 13

def readdict():
    data = open("data/dict_en.txt").read().splitlines()
    return ["then", "with", "without", "on", "and", "just", "we", "at", "as", "the", "to", "in", "new", "sky", "for", "our", "all", "one", "two", "six", "ten"] + sorted(data, key=len, reverse=True)

def autoword(text):
    dic = readdict()
    i = 0

    while i < len(text):
        for word in dic:
            if len(word) > 0 and text[i:i+len(word)] == word:
                text = text[:i+len(word)] + " " + text[i+len(word):]
                i += len(word)
                break
        i += 1
    return text

if __name__ == "__main__":
    text = common.argfiletext()
    # strip spaces
    text = text.replace(" ", "")
    # add spaces when word found
    print("Autowording, please wait...", file=sys.stderr)
    print(autoword(text))
