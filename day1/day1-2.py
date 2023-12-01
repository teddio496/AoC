f = open("day1input2.txt", "r")
result = 0
str_nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


for text in f:
    i = 0
    j = len(text) - 1
    while not text[i].isdigit() and text[i:i+3] not in str_nums and text[i:i+4] not in str_nums and text[i:i+5] not in str_nums:
        i += 1
    if text[i].isdigit():
        result += int(text[i]) * 10
    elif text[i:i+3] in str_nums:
        result += (str_nums.index(text[i:i+3]) + 1)*10
    elif text[i:i+4] in str_nums:
        result += (str_nums.index(text[i:i+4]) + 1)*10
    else:
        result += (str_nums.index(text[i:i+5]) + 1)*10

    while not text[j].isdigit() and text[j-2:j+1] not in str_nums and text[j-3:j+1] not in str_nums and text[j-4:j+1] not in str_nums:
        j -= 1
    if text[j].isdigit():
        result += int(text[j])
    elif text[j-2:j+1] in str_nums:
        result += (str_nums.index(text[j-2:j+1]) + 1)
    elif text[j-3:j+1] in str_nums:
        result += (str_nums.index(text[j-3:j+1]) + 1)
    else:
        result += (str_nums.index(text[j-4:j+1]) + 1)

print(result)