def str_str(text, pattern):
    n = len(text)
    m = len(pattern)
    d = 1 << (m - 1)
    rolling_hash = 0
    pattern_hash = 0
    
    if n < m:
        return -1
    for i in range(m):
        rolling_hash = (rolling_hash << 1) + ord(text[i])
        pattern_hash = (pattern_hash << 1) + ord(pattern[i])
    for i in range(n - m + 1):
        if rolling_hash == pattern_hash and text[i : i + m] == pattern:
            return i;
        elif i < n - m:
            rolling_hash = ((rolling_hash - ord(text[i]) * d) << 1) + ord(text[i + m])
    return -1

if __name__ == '__main__':
    ex_0 = str_str("text", "pattern")
    ex_1 = str_str("text", "text")
    ex_2 = str_str("foobar", "ar")
    ex_3 = str_str("foobar", "ob")
    pass
