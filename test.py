def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    i = 0
    while i < len(strarr) - k:
        strarr[i]  = ''
        x = i
        while x <= i + k:
            strarr[i] = strarr[i] + strarr[x]
            x = x + 1
            print(x)
        i = i + 1

longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2),

