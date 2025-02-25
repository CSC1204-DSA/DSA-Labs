"""
Given a string and a pattern, this code finds all occurrences of the pattern in the string.

Example:
--------
string = "AABAACAADAABAABA", pattern = "AABA"
Outputs indices: [0, 9, 12]
"""


def naive_pattern_matching(string, pattern):
    """
    Naive approach:
    1. Slide over 'string' in windows of size equal to len(pattern).
    2. For each window, compare each character with the corresponding character in 'pattern'.
    3. If all match, record the start index.

    Time Complexity: O(n*m) where n = len(string), m = len(pattern).
    """
    matched_indices = []
    flag = 0
    m = len(pattern)

    # Slide the window from index 0 to len(string) - m
    for i in range(len(string) - m + 1):
        k = 0
        # Check all characters in the current window
        for j in range(i, i + m):
            if pattern[k] != string[j]:
                flag = 1
                break
            else:
                k += 1
        # If we didn't break early, it means the pattern matched fully
        if flag == 0:
            matched_indices.append(i)
        flag = 0  # Reset flag for the next window

    return matched_indices if matched_indices else None


string = "AABAACAADAABAABA"
pattern = "AABA"
print(f"Naive Method: Pattern found at {naive_pattern_matching(string, pattern)}")


# Output: Pattern found at [0, 9, 12]


def rabin_karp(string, pattern, prime):
    """
    Rabin-Karp Algorithm:
    1. Compute the hash value of 'pattern' and the first window of 'string'.
    2. Slide over the string:
       a) If current window's hash matches 'pattern' hash, compare characters to confirm.
       b) Recalculate the hash for the next window using the formula:
          hash( txt[s+1 .. s+m] ) = ( d*( hash( txt[s .. s+m-1] ) - txt[s]*h ) + txt[s+m] ) mod q
         where:
            * d is the number of characters in the input alphabet (assume 256).
            * q is a prime number (to reduce collisions).
            * h is d^(m-1) % q, used for removing the contribution of the leading character.

    Time Complexity:
        * Worst Case  : O(n*m)
        * Average Case: O(n+m)
    Returns a list of indices where the pattern is found in the string.
    """
    n = len(string)
    m = len(pattern)
    d = 256  # Number of characters in the input alphabet
    matched_indices = []

    # 'h' will be "d^(m-1) mod prime"
    h = 1
    for _ in range(m - 1):
        h = (h * d) % prime

    # Calculate initial hash values for the pattern (p) and first window (t) in the string
    p = 0  # Hash value for pattern
    t = 0  # Hash value for the first window of the string
    for i in range(m):
        p = (p * d + ord(pattern[i])) % prime
        t = (t * d + ord(string[i])) % prime

    # Slide over the string in windows of length 'm'
    for i in range(n - m + 1):
        # If the hash values match, compare character by character for confirmation
        if p == t:
            flag = 0
            for j in range(m):
                if pattern[j] != string[i + j]:
                    flag = 1
                    break
            if flag == 0:
                matched_indices.append(i)

        # Recalculate hash for the next window if not at the end
        if i < n - m:
            # Remove the leading character's contribution and add the new trailing character
            t = ((t - ord(string[i]) * h) * d + ord(string[i + m])) % prime

            # If the new hash is negative, convert it to positive by adding 'prime'
            if t < 0:
                t += prime

    return matched_indices


print(f"Rabin-Karp Method: Pattern found at {rabin_karp(string, pattern, 11)}")
# Output: Pattern found at [0, 9, 12]
