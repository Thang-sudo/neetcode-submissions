class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        results = []
        # Get the original index 
        for i, t in enumerate(tasks):
            t.append(i)
        # Sort by enqueueTime in descending 
        tasks.sort(key=lambda t: t[0])
        # for each cycle, push all tasks with enqueueTime equals or less than to the cycle number to the minheap
        min_heap = []
        i, currentTime = 0, 0
        # Process while we still have queued tasks or pending tasks
        while min_heap or i < len(tasks):
            # Queue all tasks with enqueuedTime <= currentTime
            while i < len(tasks) and tasks[i][0] <= currentTime:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            # if none of the task enqueuedTime ready, drag the time to the earliest task
            if not min_heap:
                currentTime = tasks[i][0]
            # process all ready tasks
            else:
                proctime, index = heapq.heappop(min_heap)
                # Add the processing time of the task to the current time
                currentTime += proctime
                results.append(index)
        return results

                




        
