#1
def count_vowels(s):
    s = s.lower()
    vowels = "aeiou"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    print(count)


#2
def reverse_list(items):
    new_list = []
    for i in range(len(items) - 1, -1, -1):
        new_list.append(items[i])
    print(new_list)


#3
def first_and_last(s):
    if len(s) == 1:
        print(s + s)
    else:
        print(s[0] + s[-1])


#4
def join_with_dash(words):
    result = words[0]
    for i in range(1, len(words)):
        result = result + "-" + words[i]
    print(result)


#5
def remove_spaces(text):
    result = ""
    for ch in text:
        if ch != " ":
            result = result + ch
    print(result)
