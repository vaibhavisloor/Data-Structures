class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.completion = 0
        self.turnaround = 0
        self.waiting = 0


def fcfs(processes):
    processes.sort(key = lambda x : x.arrival)
    process_index = -1
    last_completed = 0
    for process in processes:
        process_index += 1
        if process_index == 0:
            process.completion = process.burst
            process.turnaround = process.completion
        
        else:
            if process.arrival >= last_completed:
                process.completion = process.arrival + process.burst
                process.turnaround = process.burst
            else:
                process.waiting = last_completed - process.arrival
                process.turnaround = process.waiting + process.burst
                process.completion = process.arrival + process.turnaround

        last_completed = process.completion

def sjf(processes):
    pass

def round_robin(processes, quantum):

    # TODO: use a queue, time-slice each process
    pass


def print_table(processes):
    print(f"{'PID':<5}{'AT':<5}{'BT':<5}{'CT':<5}{'TAT':<5}{'WT':<5}")
    for p in processes:
        print(f"{p.pid:<5}{p.arrival:<5}{p.burst:<5}{p.completion:<5}{p.turnaround:<5}{p.waiting:<5}")
    
    n = len(processes)
    avg_wt = sum(p.waiting for p in processes) / n
    avg_tat = sum(p.turnaround for p in processes) / n
    print(f"\nAvg Waiting Time:    {avg_wt:.2f}")
    print(f"Avg Turnaround Time: {avg_tat:.2f}")


# Test input
if __name__ == "__main__":
    procs = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
        Process("P4", 3, 6),
    ]
    
    fcfs(procs)
    print_table(procs)