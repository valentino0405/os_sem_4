def sjf_scheduling(processes, arrival_time, burst_time):
    n = len(processes)

    process_details = [(processes[i], arrival_time[i], burst_time[i]) for i in range(n)]
    process_details.sort(key=lambda x: x[1])

    current_time = 0
    completed = 0
    total_tat = 0
    total_wt = 0

    table = []
    gantt_chart = []

    while completed < n:
        available_processes = [p for p in process_details if p[1] <= current_time and p[1] != -1]

        if available_processes:
            available_processes.sort(key=lambda x: x[2])
            process = available_processes[0]

            finish_time = current_time + process[2]
            tat = finish_time - process[1]
            wt = tat - process[2]

            total_tat += tat
            total_wt += wt

            table.append([process[0], process[1], process[2], finish_time, tat, wt])
            gantt_chart.append((process[0], current_time, finish_time))

            process_details = [p if p[0] != process[0] else (p[0], -1, p[2]) for p in process_details]
            current_time = finish_time
            completed += 1
        else:
            current_time += 1

    avg_tat = total_tat / n
    avg_wt = total_wt / n

    print("Process\tArrivalTime\tBurstTime\tFinishTime\tTurnaroundTime\tWaitingTime")

    for row in table:
        print("\t\t\t".join(map(str, row)))

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    print("\nGantt Chart:")

    max_time = max(finish_time, current_time)

    timeline = "|"
    for process, start, end in gantt_chart:
        timeline += f"{start}----{process}----{end}|"

    print(timeline)


def main():
    num_processes = int(input("Enter the number of processes: "))

    processes = []
    for i in range(num_processes):
        processes.append(input(f"Enter the name for process {i + 1}: "))

    arrival_time = []
    for i in range(num_processes):
        arrival_time.append(int(input(f"Enter the arrival time for {processes[i]}: ")))

    burst_time = []
    for i in range(num_processes):
        burst_time.append(int(input(f"Enter the burst time for {processes[i]}: ")))

    sjf_scheduling(processes, arrival_time, burst_time)


if __name__ == "__main__":
    main()