from collections import deque

def round_robin_scheduling(processes, arrival_time, burst_time, quantum):
    n = len(processes)
    remaining_burst_time = burst_time[:]  # Copy burst time
    process_details = [(processes[i], arrival_time[i], burst_time[i]) for i in range(n)]
    process_details.sort(key=lambda x: x[1])  # Sort by arrival time

    current_time = 0
    total_tat = 0
    total_wt = 0
    table = []
    gantt_chart = []
    queue = deque()
    completed_processes = 0
    visited = [False] * n

    while completed_processes < n:
        for i in range(n):
            process, at, bt = process_details[i]
            if at <= current_time and remaining_burst_time[i] > 0 and not visited[i]:
                queue.append(i)
                visited[i] = True

        if queue:
            idx = queue.popleft()
            process, at, bt = process_details[idx]
            time_slice = min(quantum, remaining_burst_time[idx])
            remaining_burst_time[idx] -= time_slice
            gantt_chart.append((process, current_time, current_time + time_slice))
            current_time += time_slice

            # Check again if any new process has arrived during this time slice
            for i in range(n):
                process_i, at_i, _ = process_details[i]
                if at_i <= current_time and remaining_burst_time[i] > 0 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

            if remaining_burst_time[idx] > 0:
                queue.append(idx)  # Re-add process if not completed
            else:
                finish_time = current_time
                tat = finish_time - at
                wt = tat - bt
                total_tat += tat
                total_wt += wt
                completed_processes += 1
                table.append([process, at, bt, finish_time, tat, wt])
        else:
            current_time += 1  # Idle time

    avg_tat = total_tat / n
    avg_wt = total_wt / n

    print("Process\tArrivalTime\tBurstTime\tFinishTime\tTurnaroundTime\tWaitingTime")
    for row in table:
        print("\t".join(map(str, row)))

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    print("\nGantt Chart:")
    timeline = "|"
    for process, start, end in gantt_chart:
        timeline += f"{start}--{process}--{end}|"
    print(timeline)

def main():
    num_processes = int(input("Enter the number of processes: "))
    processes = [input(f"Enter the name for process {i+1}: ") for i in range(num_processes)]
    arrival_time = [int(input(f"Enter the arrival time for {processes[i]}: ")) for i in range(num_processes)]
    burst_time = [int(input(f"Enter the burst time for {processes[i]}: ")) for i in range(num_processes)]
    quantum = int(input("Enter the time quantum: "))
    round_robin_scheduling(processes, arrival_time, burst_time, quantum)

if __name__ == "__main__":
    main()
