import re

def main():
    total = 0
    with open("./inputs/1.txt", "r") as file:
        data = file.read().splitlines()

        for line in data:
            total += getCalibration(line)
    
    print(total)

def getCalibration(line:str):
    first = getStringVal(line, True)
    second = getStringVal(line, False)
    print(line, first, second, first * 10 + second)
    return first * 10 + second

def getStringVal(line:str, first: bool) -> (int):
    indicies = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
                # part two
                "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    bestIndex = -1
    bestValue = 0
    for i, sub in enumerate(indicies):
        try:
            if first:
                index = line.index(sub)
                if index < bestIndex or bestIndex == -1:
                    bestIndex = index
                    bestValue = i
            else:
                index = line.rindex(sub)
                if index > bestIndex or bestIndex == -1:
                    bestIndex = index
                    bestValue = i
        except ValueError:
            continue
    print("line: "+ line, (bestValue % 9) + 1)
    return (bestValue % 9) + 1

main()