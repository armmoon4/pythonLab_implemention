def missingCharacters(s):
    digits = set('0123456789')
    letters = set('abcdefghijklmnopqrstuvwxyz')
    present = set(s)
    missing_digits = ''.join(sorted(digits - present))
    missing_letters = ''.join(sorted(letters - present))
    return missing_digits + missing_letters
s = input()
result = missingCharacters(s)
print(result)
