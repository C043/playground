class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats = 0
        while left <= right:
            if people[right] + people[left] > limit:
                right -= 1
            else:
                right -= 1
                left += 1

            boats += 1

        return boats


people = [1, 2]
people = [3, 2, 2, 1]
limit = 3

solution = Solution()
print(solution.numRescueBoats(people, limit))
