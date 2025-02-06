from itertools import permutations

for i in permutations("abcd"):
    print(" > ".join(i))