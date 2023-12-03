f = open("day2input.txt", "r")
def check_validity(lst: list) -> bool:
    for i in lst:
        if i[-1] == "e" and int(i.split()[0]) > 14:
            return False
        if i[-1] == "n" and int(i.split()[0]) > 13:
            return False
        if i[-1] == "d" and int(i.split()[0]) > 12:
            return False
    return True
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
    if check_validity(temp):
        result += int(game_num)
        print(check_validity(temp))
print(result)

