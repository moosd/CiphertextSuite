#!/usr/bin/env python3

# Caesar shift (w/ optional frequency analysis)
# by moosd 2015

import sys
import common, freqanalysis

def caesar(text, shift):
    text = text.lower()
    deciph = ""
    for c in text:
        val = ((ord(c) - ord('a') + shift) % 26) + ord('a')
        deciph += c if ord(c) > ord('z') or ord(c) < ord('a') else str(chr(val))
    return deciph

# do stuff if run manually
if __name__ == "__main__":
    text = common.argfiletext()
    shift = None

    if len(sys.argv) > 2:
        shift = int(sys.argv[2])
    else:
        shift = -freqanalysis.simpleshift(text) # do shift in reverse

    # print result
    print(caesar(text, shift))
