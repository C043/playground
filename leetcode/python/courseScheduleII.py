from collections import deque
from typing import Dict, List, Set


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
            return []

        # While there are courses in the queue with 0 deps, we pop one and we add one to the done counter
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            doneCounter += 1

            # For every successor in the adjList of the course that we just popped, we remove one from the depCountMap of the successor and if it's 0, we append the successor to the queue since that course has 0 deps now.
            for successor in adjList[course]:
                depCountMap[successor] -= 1
                if depCountMap[successor] == 0:
                    queue.append(successor)

        # We return true if the doneCounter is equal to the numCourses, otherwise there was a loop and the doneCounter is less than the numCoureses
        return result if doneCounter == numCourses else []


numCourses = 2
prerequisites = [[1, 0], [0, 1]]
numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
solution = Solution()
print(solution.findOrder(numCourses, prerequisites))

"""
Khan's algorithm consists in these steps:
- Create a dependency count map where for each course, we count how many dependency it needs
- Dependency list where for each course we store a set with every dependency
- We populate these two dict
- We start the doneCounter to track the number of courses completed
- We start an empty queue
- For every course with no dependency, we add the course in the queue
- If the queue is still empty it means the doing every course is not possible
- Finally, we process the queue, every course in the queue can be completed so we add it to the result list
- Then we reduce by one the dependency counter from every course that had the current course as a dependency as we just completed it
- If the new dependency counter is 0, we put that course in the queue
- We return the result list if its length is equal to the number of courses we need to complete, we return an empty list otherwise
"""
