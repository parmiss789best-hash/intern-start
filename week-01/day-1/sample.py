def to_binary(n):
    if n == 0:
        return "0"

    bits = ""
    while n > 0:
        bits = str(n % 2) + bits
        n = n // 2

    return bits


to_binary(12)
