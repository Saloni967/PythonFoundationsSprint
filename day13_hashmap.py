def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True


s = input("Enter first string: ")
t = input("Enter second string: ")

if is_anagram(s, t):
    print("They are anagrams")
else:
    print("They are not anagrams")