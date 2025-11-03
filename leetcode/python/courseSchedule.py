from collections import deque
from typing import Dict, List, Set


class Solution:
    # DFS iteratively
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependencyList: Dict[int, List[int]] = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            dependencyList[course].append(prerequisite)

        visited: Set[int] = set()
        visiting: Set[int] = set()

        for course in range(numCourses):
            if course not in visited:
                stack: List[int] = [course]
                while stack:
                    currentCourse = stack[-1]
                    if currentCourse not in visiting:
                        visiting.add(currentCourse)

                    pushedPrereq = False
                    for prerequisite in dependencyList[currentCourse]:
                        if prerequisite in visiting:
                            return False
                        elif prerequisite not in visited:
                            stack.append(prerequisite)
                            pushedPrereq = True
                            break
                    if not pushedPrereq:
                        stack.pop()
                        visited.add(currentCourse)
                        visiting.remove(currentCourse)

        return True

    # DFS Recursive
    def canFinishDFSRecursive(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        dependencyList: Dict[int, List[int]] = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            dependencyList[course].append(prerequisite)

        visiting: Set[int] = set()
        visited: Set[int] = set()

        for course in range(numCourses):
            isValid = self.checkDependencies(course, dependencyList, visiting, visited)
            if not isValid:
                return False

        return True

    def checkDependencies(
        self,
        course: int,
        dependencyList: Dict[int, List[int]],
        visiting: Set[int],
        visited: Set[int],
    ) -> bool:
        if course in visiting:
            return False

        if course in visited:
            return True

        visiting.add(course)
        for dep in dependencyList[course]:
            isValid = self.checkDependencies(dep, dependencyList, visiting, visited)
            if not isValid:
                return False

        visiting.remove(course)
        visited.add(course)

        return True

    def canFinishKahn(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree: Dict[int, int] = {i: 0 for i in range(numCourses)}
        adjList: Dict[int, Set[int]] = {i: set() for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            inDegree[course] += 1
            adjList[prerequisite].add(course)

        done: Set[int] = set()
        queue: deque[int] = deque()

        for course, depCount in inDegree.items():
            if depCount == 0:
                queue.append(course)

        if not queue:
            return False

        while queue:
            course = queue.popleft()
            done.add(course)

            for successor in adjList[course]:
                inDegree[successor] -= 1
                if inDegree[successor] == 0:
                    queue.append(successor)

        return len(done) == numCourses


solution = Solution()
print(solution.canFinishKahn(2, [[1, 0], [0, 1]]))
print(solution.canFinishKahn(2, [[1, 0]]))

"""
The first two implementations use DFS to get to the solution.
The first is iterative and the second is recursive.
The recursive one is better because it splits the logic in two, making the whole algorithm more readable.

The time complexity is O(v + e) where v is the number of courses (vertices) and e is the number of dependencies (edges) for each course.
Building the depList takes O(e) time because we iterate through all the edges once
The DFS traversal visits all the vertices and edges once. The outer loop runs v times.

The space complexity is O(v + e) because we keep in memory all the cources once in the visited set (O(v)). Also we keep in memory the depList which takes O(e) space.

TODO: Reflect on the kahn's algo implementation
"""
