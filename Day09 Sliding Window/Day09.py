datas = []
blockDatas = []

with open("day9.txt", "r") as file:
    for line in file:
        datas.append(list(line.strip()))

# Example numbers, possibly checksums or identifiers
# 6344411696125
# 6363268339304

def calCheckSum(data):
    total_sum = 0
    for i in range(len(data)):
        if data[i] == ".":
            continue
        sum = i * int(data[i])
        total_sum += sum
    print(total_sum)

def shiftBlocks(data):
    leftP = 0
    rightP = len(data) - 1

    while leftP < rightP:
        while leftP < rightP and data[leftP] != ".":
            leftP += 1
        while data[rightP] == "." and rightP > leftP:
            rightP -= 1
        if rightP <= leftP:
            break
        toReplace = int(data[rightP])
        data[leftP] = toReplace
        data[rightP] = "."
        rightP -= 1
    calCheckSum(data)

def checkSpace(data, index):
    for i in range(len(data), index):
        if data[i] == ".":
            return True
    return False

def shiftBlocks2(data):
    processed_files = {}
    rightP = len(data) - 1

    while rightP > 0:
        # Find the end of the current file block
        replaceEnd = rightP
        curFile = data[replaceEnd]

        # Find the start of the current file block
        replaceStart = replaceEnd
        while replaceStart > 0 and data[replaceStart - 1] == curFile:
            replaceStart -= 1

        if checkSpace(data, replaceStart):
            break

        replaceWinSize = replaceEnd - replaceStart + 1
        availPStart = 0
        foundSpace = False

        # Find a contiguous block of free space
        while availPStart < replaceStart and availPStart < rightP:
            while availPStart < replaceStart and data[availPStart] != ".":
                availPStart += 1

            if availPStart == len(data):
                break

            availPEnd = availPStart
            while availPEnd + 1 < replaceStart and data[availPEnd + 1] == ".":
                availPEnd += 1

            curAvailSize = availPEnd - availPStart + 1
            if curAvailSize >= replaceWinSize:
                foundSpace = True
                break
            else:
                availPStart = availPEnd + 1

        if foundSpace:
            for i in range(replaceWinSize):
                data[availPStart + i] = curFile
            availPStart += 1
            data[replaceEnd] = "."
            replaceEnd -= 1
        else:
            rightP = replaceStart - 1

        # Mark the file as processed
        processed_files[curFile] = True

    calCheckSum(data)
    # print(data)


def inputLine(data):
    newData = []
    counter = 0
    for i in range(len(data)):
        curVal = int(data[i])
        if i % 2 == 0:
            j = 0
            while j < curVal:
                newData.append(counter)
                j += 1
            counter += 1
        else:
            j = 0
            while j < curVal:
                newData.append(".")
                j += 1

    shiftBlocks2(newData)


inputLine(datas[0])

