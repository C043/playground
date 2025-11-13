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


"""
This is an implementation of Dijkstra's Algorithm where we only get the minimum distance, not the route. (The problem did not require the route)

- From the distances list we build the adjacency list, the weighted graph.
- We create the distances dict and put default value inf and value ofr the starting node as 0 because from the starting node there is 0 distance while we don't know the min distance to the other nodes yet.
- We use a min heap that starts with a tuple (distance, startingNode) to keep track of the nodes with the distance it takes to get there from the starting node.
- Until the heap is not empty, we take the min distance node from it and we calculate the new time for each of its neighbors (current time to get to that neighbor + time it takes to get to the current node we just popped). If it's less than the one already in our distances dict, we update it. If it's not, it means that there is another shorter way to get there.
- After this, we calculate the max value from all the dict's values and return it if it's not inf.

The time complexity is O(n log e)
where n is the number of nodes and e is the number of edges
This is because we use O(e) time for the graph construction loop that runs once for each edge
Then in the main while loop, we do up to n heapppop operations and up to e heappush operations
Each takes O(log n) time. This results in a total time complexity of O(n log n + e log n), which simplifies to O(e log n) for a connected graph

The space complexity is O(n + e)
where n is the number of nodes and e is the number of edges.
- This is because we effectively recreate the graph from the times list so we save each node and a reference to that node for each edge. O(e)
- We also create a distances dict wich contains all the nodes. O(n)
"""
