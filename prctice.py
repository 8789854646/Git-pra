string=["hello",12,45.6,89,"world"]

sentence="hello world welcome to python and python is programming language"

words = sentence.split()
print(words)

d = {word: len(word) for word in words}
print(d)


s_sort = sorted(d.items(), key = lambda item: item[-1])
print(s_sort[-1])