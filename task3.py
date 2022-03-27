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
    if revers:
        words_l = list(reversed(args))
        words = ''.join(words_l)
        return words
    else:
        words = ''.join(args)
        return words


concatenated = concat('Hi', ' ', 'world', revers=True)
print(concatenated)
