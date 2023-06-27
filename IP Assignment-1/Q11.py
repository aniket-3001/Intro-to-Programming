'''
Q. Take as input, an integer followed by email addresses. Your task is to print only valid email addresses in lexicographical order.


Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores 
The website name can only have letters (both uppercase and lowercase) and digits
The extension can only contain letters (both uppercase and lowercase)
The maximum length of the extension is 3

Sample Input

3
lara@hackerrank.com
aniket22073@iiitd.ac.in
britts_54@hackerrank.com

Sample Output

lara@hackerrank.com
britts_54@hackerrank.com
'''

# code begins here


def length(s):
    len = 0
    for c in s:
        len += 1
    return len


def alpha_check(str):
    ans = True
    for c in str:
        if ord(c) < 65 or (ord(c) > 90 and ord(c) < 97) or ord(c) > 122:
            ans = False
            return ans
    return ans


def alpha_num_check(str):
    ans = True
    for c in str:
        if ord(c) < 48 or (ord(c) > 57 and ord(c) < 65) or (ord(c) > 90 and ord(c) < 97) or ord(c) > 122:
            ans = False
            return ans
    return ans


def alpha_num_dash_check(str):
    ans = True
    for c in str:
        if ord(c) < 45 or (ord(c) > 45 and ord(c) < 48) or (ord(c) > 57 and ord(c) < 65) or (ord(c) > 90 and ord(c) < 95) or (ord(c) > 95 and ord(c) < 97) or ord(c) > 122:
            ans = False
            return ans
    return ans


def email_check(s):
    ans = True
    username = ""
    website = ""
    ext = ""
    at = 0
    dot = 0
    ctr_at = 0
    ctr_dot = 0
    for i in range(length(s)):
        if s[i] == "@":
            at = i
            ctr_at += 1
        elif s[i] == ".":
            dot = i
            ctr_dot += 1
    username = s[0:at]
    website = s[at+1:dot]
    ext = s[dot+1:]
    if length(ext) > 3:
        ans = False
        return ans
    elif ctr_dot > 1 or ctr_at > 1:
        ans = False
        return ans
    elif not alpha_check(ext) or not alpha_num_check(website) or not alpha_num_dash_check(username):
        ans = False
        return ans
    return ans


emails = []
n = int(input("enter number of email addresses you want to check: "))
for i in range(n):
    ele = input("enter email address: ")
    emails += [ele]

for i in emails:
    if email_check(i):
        print(i)
