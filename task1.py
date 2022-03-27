def concat(*args: str, reversed=False, sep=' '):
    words = [word for word in args]
    if reversed:
        words.reverse()
    print(*words)


concat('Hi', "I'm", 'Mary', reversed=False)
