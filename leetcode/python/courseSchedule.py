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
        # We create two maps: one to count how many deps a course has where the key is the course and the value is the int
        # One to have the list of deps for a specified course: course as a key and set as value
        depCountMap: Dict[int, int] = {i: 0 for i in range(numCourses)}
        adjList: Dict[int, Set[int]] = {i: set() for i in range(numCourses)}

        # For every course and prerequisite, add one to the count of the course and add course to the list of dependencies of the dependency
        for course, prerequisite in prerequisites:
            depCountMap[course] += 1
            adjList[prerequisite].add(course)

        doneCounter = 0
        queue: deque[int] = deque()

        # We add to the queue all the courses that have 0 deps
        for course, depCount in depCountMap.items():
            if depCount == 0:
                queue.append(course)

        if not queue:
            return False

        # While there are courses in the queue with 0 deps, we pop one and we add one to the done counter
        while queue:
            course = queue.popleft()
            doneCounter += 1

            # For every successor in the adjList of the course that we just popped, we remove one from the depCountMap of the successor and if it's 0, we append the successor to the queue since that course has 0 deps now.
            for successor in adjList[course]:
                depCountMap[successor] -= 1
                if depCountMap[successor] == 0:
                    queue.append(successor)

        # We return true if the doneCounter is equal to the numCourses, otherwise there was a loop and the doneCounter is less than the numCoureses
        return doneCounter == numCourses


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

The Kahn's algorithm implementation time and space complexities are the same as the DFS but the Kahn's implementation returns the valid order of tasks while the DFS returns only if a valid order is possible.
Use Kahn's only if you need that order.
"""
