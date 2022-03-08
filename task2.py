def fibonacci(n) -> int:
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))

# вариант без рекурсии


def fib(n):
    nums = [1] * n
    for num in range(2, n):
        nums[num] = nums[num-1] + nums[num-2]
    return nums[num]


print(fib(6))
