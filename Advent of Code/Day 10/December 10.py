import numpy as np

with open('testinputDec10.txt', 'r') as f:
    lines = f.read().strip().split()

pairs = ["()", "[]", "<>", "{}"]
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
stack = []
def parse(line):
    for char in line:
        good = False
        for symb in pairs:
            if char == symb[0]:
                stack.append(char)
                good = True
            elif char == symb[1]:
                if stack[-1] == symb[0]:
                    stack.pop()
                    good = True

        if not good:
            return scores[char]

    return 0


ans = 0
for line in lines:
    ans += parse(line)

print(ans)      

# B

with open("./inputDec10.txt") as fin:
    raw_data = fin.read().strip()
data = raw_data.split("\n")

pairs = ["()", "[]", "<>", "{}"]
bad_scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
good_scores = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def parse(line):
    stack = []
    for char in line:
        good = False
        for p in pairs:
            if char == p[0]:
                stack.append(char)
                good = True
            elif char == p[1]:
                if stack[-1] == p[0]:
                    stack.pop()
                    good = True

        if not good:
            return bad_scores[char]

    return 0


def complete(line):
    stack = []
    ans = 0
    for char in line:
        for p in pairs:
            if char == p[0]:
                stack.append(char)
            elif char == p[1]:
                if stack[-1] == p[0]:
                    stack.pop()

    for c in stack[::-1]:
        ans *= 5
        ans += good_scores[c]

    return ans


# Delete corrupted stuff
data = [line for line in data if parse(line) == 0]

scores = []
for line in data:
    scores.append(complete(line))

scores.sort()
ans = scores[len(scores) // 2]
print(ans)