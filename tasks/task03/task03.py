import re

texts = [
    "Hello, World!",
    "The world is mine",
    "Hello, how are you?"
]


# Parser for each string in an input text
def parsestr(r, st):
    res = re.findall(r'\w+', st)
    for w in res:
        wl = w.lower()
        if wl in d:
            drn, dcnt = d[wl]
            d[wl] = (drn, dcnt+1)
        else:
            d[wl] = (r, 1)


# Main code
d = {}
for rn, s in enumerate(texts):
    parsestr(rn, s)

# Settings for print
allignsize = 15
wrd = "word"
wrdPostfix = (allignsize-len(wrd))*" "
cnt = "count"
cntPostfix = (allignsize-len(cnt))*" "
fl = "first line"

print(wrd, wrdPostfix, cnt, cntPostfix, "first line")

for i in d.items():
    word, (rn, qty) = i
    wordPostfix = (allignsize-len(word))*" "
    qtyPostfix = (allignsize-len(str(qty)))*" "
    print(word, wordPostfix, qty, qtyPostfix, rn)
