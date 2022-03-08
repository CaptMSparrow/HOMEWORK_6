def inspect(f):
    def wrapp(*args, **kwargs):
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        words = [word for word in args]
        if kwargs:
            words.reverse()
            print('Retvalue: ', *words)
        else:
            print('Retvalue: ', *words)
        return f(*args, **kwargs)
    return wrapp


@inspect
def f(*args, reversed=False):
    words = [word for word in args]
    if reversed:
        words.reverse()
        print(*words)
    else:
        print(*words)


f('Hi', ' ', 'world', reversed=True)
