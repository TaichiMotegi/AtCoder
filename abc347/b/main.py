s = input().strip()
substrings = set()

for i in range(len(s)):
    for j in range(1, len(s) - i + 1):
        substrings.add(s[i : i + j])

print(len(substrings))
