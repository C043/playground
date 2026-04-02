from collections import deque
from typing import Deque, List, Set


def shortest_transformation_sequence(
    start: str, end: str, dictionary: List[str]
) -> int:
    # We transform the dictionary in a set so we can access the elements in constant time
    dictionary_set = set(dictionary)

    # If start or end are not in the dictionary, this problem is unsolvable
    if start not in dictionary_set or end not in dictionary_set:
        return 0
    if start == end:
        return 1

    # We find every possible next word word in which only one letter changes
    # We check if we did not visited the new word and if the new word is in the dictionary
    # If so, we append the new word to the queue and keep going until the queue is empty
    lower_case_alphabet = "abcdefghijklmnopqrstuvwxyz"
    queue: Deque[str] = deque([start])
    visited: Set[str] = set([start])
    dist = 0
    while queue:
        for _ in range(len(queue)):
            curr_word = queue.popleft()
            # If the current word is equal to the end word, we've found the solution
            if curr_word == end:
                return dist + 1
            for i in range(len(curr_word)):
                for c in lower_case_alphabet:
                    next_word = curr_word[:i] + c + curr_word[i + 1 :]
                    if next_word in dictionary_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append(next_word)
        # When we processed on word, before going to the next on, we add one to the solution because we're getting away from the start
        dist += 1

    return 0


start = "red"
end = "hit"
dictionary = ["red", "bed", "hat", "rod", "rad", "rat", "hit", "bad", "bat"]
print(shortest_transformation_sequence(start, end, dictionary))

"""
Time complexity is O(n*L2) where n denotes the number of words in the dictionary, and L denotes the length of a word.
- Creating a hash set containing all the words in the dictionary takes O(n*L) time, because hashing each of the n words takes O(L) time
- Level-order traversal processes at most n words from the dictionary. At each of these words we generate up to 26 * L transformations, ant it takes O(L) time to check if a transformation exists in the visited and dictionary_set hash, and to enqueue it. This means level order traversal takes approximately O(n * 26 * L * L) = O(n * L2) time
Therefore, the overall time complexity is O(n*L) + O(n*L2) = O(n * L2)

Space complexity is O(n*L) taken up by the dictionary_set hash set, the visited hash set, and the queue
"""
