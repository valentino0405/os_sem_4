def main():
    k = 0
    a = 0
    b = 0
    instance = [0] * 5
    availability = [0] * 5
    allocated = [[0 for _ in range(5)] for _ in range(10)]
    need = [[0 for _ in range(5)] for _ in range(10)]
    MAX = [[0 for _ in range(5)] for _ in range(10)]
    P = [0] * 10
    op = [0] * 10

    no_of_resources = int(input("Enter the number of resources: "))

    print("\nEnter the max instances of each resource")
    for i in range(no_of_resources):
        availability[i] = 0
        instance[i] = int(input(f"{chr(97 + i)} = "))

    process = int(input("\nEnter the number of processes: "))

    print("\nEnter the allocation matrix")
    for i in range(no_of_resources):
        print(f" {chr(97 + i)}", end='')
    print()

    for i in range(process):
        P[i] = i
        print(f"P[{P[i]}] ", end='')
        row = list(map(int, input().split()))
        for j in range(no_of_resources):
            allocated[i][j] = row[j]
            availability[j] += allocated[i][j]

    print("\nEnter the MAX matrix")
    for i in range(no_of_resources):
        print(f" {chr(97 + i)}", end='')
        availability[i] = instance[i] - availability[i]
    print()

    for i in range(process):
        print(f"P[{i}] ", end='')
        row = list(map(int, input().split()))
        for j in range(no_of_resources):
            MAX[i][j] = row[j]

    # Simulating the label A:
    while True:
        a = -1
        for i in range(process):
            cnt = 0
            b = P[i]
            for j in range(no_of_resources):
                need[b][j] = MAX[b][j] - allocated[b][j]
                if need[b][j] <= availability[j]:
                    cnt += 1

            if cnt == no_of_resources:
                op[k] = P[i]
                k += 1
                for j in range(no_of_resources):
                    availability[j] += allocated[b][j]
            else:
                a += 1
                P[a] = P[i]

        if a == -1:
            break
        else:
            process = a + 1

    print("\nSafe Sequence:\n\t<", end='')
    for i in range(k):
        print(f" P[{op[i]}] ", end='')
    print(">\n")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
