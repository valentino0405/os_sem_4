def first_fit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j
                blockSize[j] -= processSize[i]
                break

    print("\nFirst Fit Allocation:")
    print("Process No.\tProcess Size\tBlock no.")
    for i in range(n):
        print(f"{i + 1}\t\t{processSize[i]}\t\t", end="")
        if allocation[i] != -1:
            print(f"{allocation[i] + 1}")
        else:
            print("Not Allocated")


def best_fit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1 or blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j
        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i]

    print("\nBest Fit Allocation:")
    print("Process No.\tProcess Size\tBlock no.")
    for i in range(n):
        print(f"{i + 1}\t\t{processSize[i]}\t\t", end="")
        if allocation[i] != -1:
            print(f"{allocation[i] + 1}")
        else:
            print("Not Allocated")


def worst_fit(blockSize, m, processSize, n):
    allocation = [-1] * n

    for i in range(n):
        wstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1 or blockSize[wstIdx] < blockSize[j]:
                    wstIdx = j
        if wstIdx != -1:
            allocation[i] = wstIdx
            blockSize[wstIdx] -= processSize[i]

    print("\nWorst Fit Allocation:")
    print("Process No.\tProcess Size\tBlock no.")
    for i in range(n):
        print(f"{i + 1}\t\t{processSize[i]}\t\t", end="")
        if allocation[i] != -1:
            print(f"{allocation[i] + 1}")
        else:
            print("Not Allocated")


def main():
    blockSize = []
    processSize = []

    m = int(input("Enter number of blocks: "))
    print("Enter block sizes:")
    for i in range(m):
        blockSize.append(int(input(f"Block {i + 1}: ")))

    n = int(input("\nEnter number of processes: "))
    print("Enter process sizes:")
    for i in range(n):
        processSize.append(int(input(f"Process {i + 1}: ")))

    first_fit(blockSize.copy(), m, processSize, n)
    best_fit(blockSize.copy(), m, processSize, n)
    worst_fit(blockSize.copy(), m, processSize, n)


if __name__ == "__main__":
    main()
