with open("day4input2.txt", "r") as file:
    result = [x for x in file.read().strip().splitlines()]

answer = 0
map = {}
for i in result:
    temp = 0
    nums = i.split(":")[1].split("|")
    pool = nums[0].split()
    picks = nums[1].split()
    for pick in picks:
        if pick in pool:
            temp += 1
    for j in temp:
        


print(answer)