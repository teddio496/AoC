f = open("day1input.txt", "r")
result = 0
for text in f:
    i = 0
    j = len(text) - 1
    while not text[i].isdigit():
        i += 1
    result += int(text[i]) * 10

    while not text[j].isdigit():
        j -= 1
    result += int(text[j])

print(result)