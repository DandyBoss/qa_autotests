#Определить, является ли строка палиндромом.

def is_palindrome(s):
    t = s.lower()
    if t[:] == t[::-1]:
        return "Yes"
    else:
        return "No"