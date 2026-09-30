class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Always handle task with the most remaining count first
        # The reason is because if we handle the tasks with fewer remaining count first then the later tasks would require alot of idle cycle because they appear to be the same task type
        # We would need to have a queue to store whether a task is ready or not
        # The cooldown queue should contain tuples. i.e (A, 3) where A is the task name and 3 is the cycle when the task is ready
        # At each iteration we pop the head of the heap to process the task with most remaining
        # take the task remaining - 1. If remaining - 1 > 0 then put it in cooldown queue
        # if the task queue[0] is ready, heappush to the heap
        # keep processing until heap or queue empty. This means there are no remaining tasks and no pending tasks
        total_cycles = 0
        cooldown_queue = deque()
        count = Counter(tasks)
        # Python only has min heap
        tasks_max_heap = [-1 * t for t in count.values()]
        heapq.heapify(tasks_max_heap)
        # Keep proccessing while we have cooldown queue or remaining task to process
        cycle = 0
        while cooldown_queue or tasks_max_heap:
            cycle += 1
            if tasks_max_heap:
                task = heapq.heappop(tasks_max_heap)
                remaining = -1 * task - 1
                if remaining > 0:
                    cooldown_queue.append((remaining, cycle + n))
            if cooldown_queue and cooldown_queue[0][1] == cycle:
                task = cooldown_queue.popleft()
                heapq.heappush(tasks_max_heap, -1 * task[0])
        return cycle
        