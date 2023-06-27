# https://www.hackerrank.com/contests/ip-lab-7-thursday/challenges/pied-piper-1-1

def compress_string(s):
    if len(s) == 0:
        return ""

    compressed_str = ""
    count = 1
    current_char = s[0]

    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            compressed_str += current_char + str(count)
            current_char = s[i]
            count = 1

    compressed_str += current_char + str(count)

    if len(compressed_str) < len(s):
        return compressed_str
    else:
        return s


s = input()
print(compress_string(s))
