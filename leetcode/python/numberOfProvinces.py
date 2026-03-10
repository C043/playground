from collections import deque
from typing import DefaultDict, List, Set


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjacencyList: dict[int, List[int]] = DefaultDict(list)
        result = 1

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if j == i:
                    continue

                if isConnected[i][j] != 0:
                    adjacencyList[i].append(j)

        queue: deque[int] = deque([0])
        visited: Set[int] = {0}

        while queue:
            city = queue.popleft()

            neighbors: List[int] = adjacencyList[city]

            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

            if not queue and len(visited) < len(isConnected):
                result += 1
                notVisited: List[int] = list(
                    set(list(range(len(isConnected)))) - visited
                )
                if notVisited:
                    queue.append(notVisited[0])
                    visited.add(notVisited[0])

        return result


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
solution = Solution()
print(solution.findCircleNum(isConnected))

"""
This solution is divided in two major sections:
- The creation of the adjacency list
- The graph traversal

The creation of the adjacency list is simple, we loop over every city edge and we append the connection to the city list of neighbors.

Once we have the adjacency list, we start a queue with the first city and start the graph traversal.
Once the queue is empty, we check if we visited every city.
If we did, it means that there is only one province.
If we did not, we find one city that we did not visited making the difference between the visited set and a list that contains the numbers from 0 to the number of cities in the isConnected list.
We add one to the result because it means that these cities are not connected to the ones in we already visited and we add the city to the queue and to visited.
The loop keep going until we visited every city. One way or another.

Time and space complexity are O(n^2)
"""
