from collections import defaultdict
from heapq import heappop, heappush
from typing import Dict, List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # adjacency list storing (time, destination)
        graph: Dict[int, List[tuple[int, int]]] = defaultdict(list)
        for start, dest, time in times:
            graph[start].append((time, dest))

        # We create the distances dict where we put deafult value inf and value of the starting node as 0
        distances = {node: float("inf") for node in range(1, n + 1)}
        distances[k] = 0

        # We initiate a heap with the starting node and its time
        heap = [(0, k)]
        # While the heap is not empty
        while heap:
            # We take the mini time node from the heap (taking the current time for that node and the value of the node)
            current_time, node = heappop(heap)

            # If the current time for that node is more than the current time for that node in the distances dict, we skip
            # This is a guard for when we already have a better time for the current node that we processed earlier
            if current_time > distances[node]:
                continue

            # For every neighbor of the current node
            for edge_time, neighbor in graph[node]:
                # We calculate the new time (current time to get to this node + time it takes to get to the neighbor from the current node)
                new_time = current_time + edge_time

                # If the new time is less than the min time we already know, we save the new time in the distances dict and push in the min heap the neighbor with the new time (that's the sum of all the other times to get to it)
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heappush(heap, (new_time, neighbor))

        # We calculate the max time from all the times in the distances dict
        max_time = max(distances.values())

        # We return the max time if the max time is not inf if it is we return -1 because it means that at least a node was not reached by the signal
        return -1 if max_time == float("inf") else int(max_time)
