import sys, os

def argfiletext():
    text = ""
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        if os.path.isfile(sys.argv[1]):
            text = open(sys.argv[1]).read()
    else:
        text = sys.stdin.read()
    return text
