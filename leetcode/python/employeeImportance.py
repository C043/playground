from collections import defaultdict, deque
from typing import Deque, List, Set


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        adjacencyList: dict[int, Employee] = {}

        while employees:
            employee = employees.pop()
            adjacencyList[employee.id] = employee

        queue: Deque[Employee] = deque([adjacencyList[id]])
        visited: Set[int] = set()
        totalImportance = 0

        while queue:
            employee = queue.popleft()

            if employee.id in visited:
                continue

            totalImportance += employee.importance

            for subId in employee.subordinates:
                queue.append(adjacencyList[subId])

            visited.add(employee.id)

        return totalImportance


employees = [Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])]
solution = Solution()
print(solution.getImportance(employees, 1))

"""
This solution is divided in two steps:
- Creating a map for quick employees lookup by id
- Looping over a queue that starts from the employee with the starting id and counting the importance of this employee and all his subordinates
We return the total importance in the end

Time complexity is O(n)
Space complexity is O(n)
"""
