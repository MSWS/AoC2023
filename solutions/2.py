colors = [12, 13, 14]
# red, green, blue

def main():
    gameSum = 0
    with open("./inputs/2.txt", "r") as file:
        data = file.read().splitlines()
        for line in data:
            gameSum += processLine(line)
    print(gameSum)

def processLine(line:str):
    gameId = int(line[len("Game "):line.index(":")])
    turns = line[line.index(":") + 2:].split(";")
    maxColors = [0, 0, 0]
    for turn in turns:
        turn = turn.strip()
        # part 1
        # for color in turn.split(","):
        #     color = color.strip()
        #     amo = int(color.split(" ")[0])
        #     maxColor = getMaxColor(color.split(" ")[1])
        #     if amo > maxColor:
        #         print(f'Game {gameId} has {amo} {color.split(" ")[1]} but max is {maxColor}')
        #         return 0

        # part 2
        for color in turn.split(","):
            color = color.strip()
            amo = int(color.split(" ")[0])
            colorIndex = getColorIndex(color.split(" ")[1])
            if amo > maxColors[colorIndex]:
                maxColors[colorIndex] = amo
    return maxColors[0] * maxColors[1] * maxColors[2]

def getMaxColor(color:str) -> int:
    return colors[getColorIndex(color)]

def getColorIndex(color:str) -> int:
    if color == "red":
        return 0
    elif color == "green":
        return 1
    elif color == "blue":
        return 2
    else:
        raise ValueError("Invalid color: " + color)

main()