from collections import defaultdict, deque
from typing import Deque, List


def prerequisites(n: int, prerequisites: List[List[int]]) -> bool:
    # Find all courses with 0 deps
    # Create the in_degrees list
    in_degrees: List[int] = [0] * n
    # Create the graph
    graph: dict[int, List[int]] = defaultdict(list)
    for i in range(len(prerequisites)):
        dep, course = prerequisites[i]
        in_degrees[course] += 1
        graph[dep].append(course)

    # Start the queue with every course that has 0 dependencies
    queue: Deque[int] = deque()
    for i in range(len(in_degrees)):
        if in_degrees[i] == 0:
            queue.append(i)

    # This variable will need to be equal to n to return True
    enrolled_courses = 0
    # We process the queue
    # For every course we pop
    # We add one to the enrolled courses
    # We decrease the in_degrees of every course that has this course as a dependency
    # If the new in_degree is now 0 we add that course to the queue because it now has 0 deps
    while queue:
        dep = queue.popleft()
        enrolled_courses += 1
        for course in graph[dep]:
            in_degrees[course] -= 1
            if in_degrees[course] == 0:
                queue.append(course)

    # In the end if we completed all courses, we return True, False otherwise
    return enrolled_courses == n


courses = [[0, 1], [0, 2], [3, 2], [1, 4], [2, 4], [4, 5]]
print(prerequisites(6, courses))

"""
Time complexity is O(n + e) where e denotes the number of edges derived from the prerequisites array.
- Creating adjacency list and recording the in-degrees takes O(e) time because we iterate through each prerequisite once
- Adding all courses with in-degree 0 to the queue takes O(n) time because we check the in-degree of each node once
- Performing Kahn's algorithm takes O(n + e) time because each course and prerequisite is processed at most once during the traversal

Space complexity is O(n + e) since the adjacency list takes up O(n + e) space, while the in_degrees array and queue each take up O(n) space
"""
