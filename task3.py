def inspect(concat):
    def wrapp(*args, **kwargs):
        print(f'Args: {args}')
        print(f'Kwargs: {kwargs}')
        retval = concat(*args, **kwargs)
        print('Retvalue:', retval)
        return retval
    return wrapp


@inspect
def concat(*args, revers=False) -> str:
    words_str = ''.join(args)
    if revers:
        words_l = list(reversed(args))
        words= ''.join(words_l)
        return words
    else:
        return words_str


concatenated = concat('Hi', ' ', 'world', revers=False)
print(concatenated)
