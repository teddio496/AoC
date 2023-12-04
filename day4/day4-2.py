with open("day4input2.txt", "r") as file:
    result = [x for x in file.read().strip().splitlines()]

answer = 0
map = {1:1}
for i in result:
    temp = 0
    nums = i.split(":")[1].split("|")
    game = int(i.split(":")[0][5:]) 
    pool = nums[0].split()
    picks = nums[1].split()

    for pick in picks:
        if pick in pool:
            temp += 1
    print(temp)
    for j in range(game+1, game + temp+1):
        map[j] = map.get(j, 1) + (map.get(game, 1))

acc = 1
for i in map.values():
    acc += i
print(acc)