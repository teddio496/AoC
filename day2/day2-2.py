f = open("day2input2.txt", "r")

result = 0
for game in f:
    temp = []
    game = game[:-1]
    new_game = list(game.split(":"))
    game_num = new_game[0][5:]
    
    for choose in new_game[1].split(";"):
        nums = choose.split(',')
        for i in range(len(nums) - 1):
            if nums[i][-2:] == "\n":
                nums[i] = nums[i][:-2]
        temp += nums
    print(temp)
    max_green = 0
    max_red = 0
    max_blue = 0

    for i in temp:
        if i[-1] == "e":
            max_blue = max(max_blue, int(i.split()[0]))
        if i[-1] == "n":
            max_green = max(max_green, int(i.split()[0]))
        if i[-1] == "d":
            max_red = max(max_red, int(i.split()[0]))

    result += max_blue*max_green*max_red


print(result)

