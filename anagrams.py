import fileinput
words = []
anagram_count = 0
for line in fileinput.input():
    words.append(sorted(line))
for word in words[1:]:
    if word == words[0]:
        anagram_count += 1
print(anagram_count)
