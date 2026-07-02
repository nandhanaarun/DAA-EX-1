# ---------------- Naive String Matching ----------------
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            matches.append(i)

    return matches


# ---------------- Rabin-Karp Algorithm ----------------
def rabin_karp(text, pattern):
    d = 256
    q = 101

    n = len(text)
    m = len(pattern)
    matches = []

    h = pow(d, m - 1, q)
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                matches.append(i)

        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q

    return matches


# ---------------- KMP Algorithm ----------------
def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    i = 0
    j = 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches


# ---------------- Main Program ----------------
text = input("Enter Text: ")
pattern = input("Enter Pattern: ")

print("\nResults:")
print("Naive Algorithm Matches at:", naive_search(text, pattern))
print("Rabin-Karp Matches at:", rabin_karp(text, pattern))
print("KMP Algorithm Matches at:", kmp_search(text, pattern))
