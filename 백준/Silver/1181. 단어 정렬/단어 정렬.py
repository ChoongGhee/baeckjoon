n = int(input())
words = []
length = []

for i in range(n):
    words.append(input())
    # length.append(len(word[i]))

words = list(set(words))
words.sort()
words.sort(key=len)

for i in range(len(words)):
    print(words[i])
