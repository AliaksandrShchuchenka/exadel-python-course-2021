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

# Print header
print(f"{'word' : <10}{'count' : <10}{'first line' : <10}")

# Print values
for i in d.items():
    word, (rn, qty) = i
    print(f"{word : <10}{qty : <10}{rn : <10}")
