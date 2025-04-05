def fcfs_scheduling(processes, arrival_time, burst_time):
    n = len(processes)
    process_details = [(processes[i], arrival_time[i], burst_time[i]) for i in range(n)]
    process_details.sort(key=lambda x: x[1])

    current_time = 0
    total_tat = 0
    total_wt = 0
    table = []
    gantt_chart = []

    for process, at, bt in process_details:
        if current_time < at:
            current_time = at
        finish_time = current_time + bt
        tat = finish_time - at
        wt = tat - bt

        total_tat += tat
        total_wt += wt

        table.append([process, at, bt, finish_time, tat, wt])
        gantt_chart.append((process, current_time, finish_time))

        current_time = finish_time

    avg_tat = total_tat / n
    avg_wt = total_wt / n

    print("Process\tArrivalTime\tBurstTime\tFinishTime\tTurnaroundTime\tWaitingTime")
    for row in table:
        print("\t\t\t".join(map(str, row)))

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    print("\nGantt Chart:")
    timeline = "|"
    for process, start, end in gantt_chart:
        timeline += f"{start}----{process}----{end}|"
    print(timeline)

def main():
    num_processes = int(input("Enter the number of processes: "))
    processes = [input(f"Enter the name for process {i+1}: ") for i in range(num_processes)]
    arrival_time = [int(input(f"Enter the arrival time for {processes[i]}: ")) for i in range(num_processes)]
    burst_time = [int(input(f"Enter the burst time for {processes[i]}: ")) for i in range(num_processes)]
    fcfs_scheduling(processes, arrival_time, burst_time)


if __name__ == "__main__":
    main()