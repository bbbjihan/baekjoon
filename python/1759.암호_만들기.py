import sys;rl=sys.stdin.readline
import itertools

L, C = map(int,rl().split())
chars = rl().split()
chars.sort()

consonants =[]
vowels = []

for char in chars:
    if char in ["a", "e", "i", "o", "u"]:
        vowels.append(char)
    else:
        consonants.append(char)

min_combis_con = list(itertools.combinations(consonants, 2))
min_combis = []
for vowel in vowels:
    for min_combi in min_combis_con:
        min_combis.append(sorted([*min_combi, vowel]))

ans = []
for min_combi in min_combis:
    remaining_chars = [char for char in chars if char not in min_combi]
    left_combis = list(itertools.combinations(remaining_chars, L - 3))
    for left_combi in left_combis:
        ans.append(''.join(sorted(left_combi + tuple(min_combi))))

ans = list(set(ans))
for line in sorted(ans):
    print(line)