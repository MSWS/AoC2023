from typing import List

lines: List[str] = []

def main():
    global lines
    with open("./inputs/3.txt", "r") as file:
        lines = file.read().splitlines()

    sum = 0

    for i in range(len(lines)):
        sum += process_line(i)
    print(sum)

def process_line(lineIndex: int):
    global lines
    line: str = lines[lineIndex]

    index = get_next_symbol(line)
    sum = 0
    while index != -1:
        size = 1
        while line[index:index+size].isnumeric() and index + size < len(line):
            size += 1

        size -= 1

        if size == 0:
            index = get_next_symbol(line, index)
            continue

        incremented = False

        if lineIndex > 0:
            if has_symbol(lines[lineIndex-1], index - 1, size + 2):
                print("inc due to prev line")
                sum += int(line[index:index+size]) # return the number
                incremented = True
        if not incremented and lineIndex < len(lines) - 1:
            if has_symbol(lines[lineIndex+1], index - 1, size + 2):
                print("inc due to next line")
                sum += int(line[index:index+size])
                incremented = True
        if not incremented and (index >= 1 and line[index-1]) != "." \
            or (index+size < len(line) and line[index+size] != "."):
            print("inc due to same line")
            sum += int(line[index:index+size])
            incremented = True

        # print(line[index:index+size], incremented)

        index += size + 1
        index = get_next_symbol(line, index)
    return sum

def get_next_symbol(line: str, start=0):
    for i, char in enumerate(line[start:]):
        if char.isnumeric():
            return start + i
    return -1


def has_symbol(line:str, index, width):
    return len(line[index:index+width].replace(".", "")) > 0

main()