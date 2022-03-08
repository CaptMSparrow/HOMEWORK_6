def concat(*args: str, reversed=False, sep=' '):
    words = []
    for word in args:
        words.append(word)
    if reversed:
        words.reverse()
        print(*words)
    else:
        print(*words)


concat('Hi', "I'm", 'Mary', reversed=True)
