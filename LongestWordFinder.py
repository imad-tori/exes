def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return (longest,len(longest))

print(longest_word(["hi","hello","world","cat"]))
print(longest_word(["apple","orange","green"]))
print(longest_word(["white","red","no"]))