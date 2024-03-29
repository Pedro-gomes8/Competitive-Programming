from heapq import heappush, heappop

# Define tasks with processing times for each machine
# For example, tasks = {"A": [3, 2, 1], "B": [2, 1, 2], "C": [1, 3, 2]} indicates each task (A, B, C) and its processing times on machines 1, 2, and 3.
tasks = {
    "A": [3, 2, 1],
    "B": [2, 1, 2],
    "C": [1, 3, 2]
}

# Initialize machine status (time when each machine will be idle)
machine_status = [0, 0, 0]

# Schedule of tasks (task_id, start_time, end_time, machine_id)
schedule = []

# Priority queue for tasks based on the next machine processing time
task_queue = []

# Initialize task queue with the first machine processing times
for task_id, times in tasks.items():
    heappush(task_queue, (times[0], task_id, 0))  # (processing_time, task_id, current_machine_index)

# Process tasks
while task_queue:
    processing_time, task_id, machine_index = heappop(task_queue)
    start_time = max(machine_status[machine_index], machine_status[machine_index - 1] if machine_index > 0 else 0)
    end_time = start_time + processing_time
    
    # Update machine status and task progress
    machine_status[machine_index] = end_time
    schedule.append((task_id, start_time, end_time, machine_index + 1))
    
    # If the task has more machines to process, add next machine processing time to the queue
    if machine_index + 1 < len(tasks[task_id]):
        next_processing_time = tasks[task_id][machine_index + 1]
        heappush(task_queue, (next_processing_time, task_id, machine_index + 1))

# Print schedule
for task in schedule:
    print(f"Task {task[0]} starts at {task[1]} and ends at {task[2]} on Machine {task[3]}")

