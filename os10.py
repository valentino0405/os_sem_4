def fcfs(nior, cy, scy):
    thm = [0] * (nior + 1)
    sum_thm = 0

    for i in range(1, nior + 1):
        if i == 1:
            thm[i] = abs(scy - cy[i])
        else:
            thm[i] = abs(cy[i - 1] - cy[i])
        sum_thm += thm[i]

    st = sum_thm / nior
    print("\n-------------------------------------")
    print("|I/O REQUEST\t\tTOTAL HEAD MOVEMENT|")
    print("-------------------------------------")
    for i in range(1, nior + 1):
        print(f"{cy[i]}\t\t\t\t\t{thm[i]}")
    print("-------------------------------------")
    print(f"AVERAGE SEEK TIME IS : {st}")
    print(f"TOTAL HEAD MOVEMENT: {sum_thm}")

def sstf(nior, cy, scy):
    dcy = cy[:]
    thm = [0] * (nior + 1)
    sum_thm = 0

    for i in range(1, nior + 1):
        min_distance = float('inf')
        min_index = -1
        for j in range(1, nior + 1):
            if dcy[j] != -1:
                distance = abs(dcy[j] - scy)
                if distance < min_distance:
                    min_distance = distance
                    min_index = j
        thm[i] = min_distance
        sum_thm += min_distance
        scy = dcy[min_index]
        dcy[min_index] = -1

    print("\n-------------------------------------")
    print("|I/O REQUEST\t\tTOTAL HEAD MOVEMENT|")
    print("-------------------------------------")
    for i in range(1, nior + 1):
        print(f"{cy[i]}\t\t\t\t\t{thm[i]}")
    print("-------------------------------------")
    st = sum_thm / nior
    print(f"AVERAGE SEEK TIME IS : {st}")
    print(f"TOTAL HEAD MOVEMENT: {sum_thm}")

def look(nior, cy, scy):
    lcy = [c for c in cy[1:] if c < scy]
    rcy = [c for c in cy[1:] if c >= scy]
    lcy.sort(reverse=True)
    rcy.sort()

    dcy = lcy + rcy  # Moving in descending order first
    thm = [0] * len(dcy)
    sum_thm = 0

    for i in range(len(dcy)):
        if i == 0:
            thm[i] = abs(scy - dcy[i])
        else:
            thm[i] = abs(dcy[i - 1] - dcy[i])
        sum_thm += thm[i]

    print("\n-------------------------------------")
    print("|I/O REQUEST\t\tTOTAL HEAD MOVEMENT|")
    print("-------------------------------------")
    for i in range(len(dcy)):
        print(f"{dcy[i]}\t\t\t\t\t{thm[i]}")
    print("-------------------------------------")
    st = sum_thm / nior
    print(f"AVERAGE SEEK TIME IS : {st}")
    print(f"TOTAL HEAD MOVEMENT: {sum_thm}")

if __name__ == "__main__":
    nior = int(input("Enter the Number of IO Requests: "))
    cy = [0] + [int(input(f"Enter Cylinder No {i + 1}: ")) for i in range(nior)]
    scy = int(input("Enter the Starting Cylinder: "))

    while True:
        print("\nDisk Scheduling Algorithms:")
        print("1. FCFS")
        print("2. SSTF")
        print("3. LOOK")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\nFCFS")
            fcfs(nior, cy, scy)
        elif choice == 2:
            print("\nSSTF")
            sstf(nior, cy, scy)
        elif choice == 3:
            print("\nLOOK")
            look(nior, cy, scy)
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please select a valid option.")
