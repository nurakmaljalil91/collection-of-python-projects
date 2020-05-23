def initial(phrase):
    words = phrase.split()
    result = ''
    for word in words:
        for w in word:
            if w.isupper():
                result += ''.join(w)
    return result

print(initial('this is my life'))