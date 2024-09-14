def revers_string(s: str) -> str:
    chars = list(s)
    l, r = 0, len(chars) - 1

    while l < r:
        chars[l], chars[r] = chars[r], chars[l]
        l += 1
        r -= 1
    return "".join(chars)


s = 'hello'
r = revers_string(s)
print(r)


