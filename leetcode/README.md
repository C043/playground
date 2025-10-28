# LeetCode Patterns Docs

This document helps link common **LeetCode problems** to the **core algorithmic patterns** they represent.  
Use it as a mental map: when you see a problem, connect it to one of these strategies.

---

## 🟩 Hashmap Pattern

### 🔹 [Two Sum](./python/twoSum.py)
- **When to use:** You need to find pairs, complements, or detect previous occurrences efficiently.
- **Key idea:** Store needed information (e.g., target - num) in a hashmap for O(1) lookup.
- **Common problems:** 
  - Two Sum
  - Subarray Sum Equals K
  - Contains Duplicate

### 🔹 [Group Anagrams](./python/groupAnagrams.py)
- **When to use:** You need to group or categorize items that share a common "signature".
- **Key idea:** Use a hashmap keyed by a normalized version of each item (e.g., sorted string).
- **Common problems:** 
  - Group Anagrams
  - Isomorphic Strings
  - Word Pattern

---

## 🟨 Stack Pattern

### 🔹 [Valid Parentheses](./python/validParenthesis.py)
- **When to use:** You need to validate nested structures or track "opening" and "closing" relationships.
- **Key idea:** Push opening elements; pop when a matching closing appears.
- **Common problems:** 
  - Valid Parentheses
  - Min Add to Make Parentheses Valid
  - Daily Temperatures (monotonic stack variant)

---

## 🟦 Sorting + Interval Pattern

### 🔹 [Merge Intervals](./python/mergeIntervals.py)
- **When to use:** You’re dealing with overlapping ranges or schedules.
- **Key idea:** Sort by start time, then merge overlapping intervals.
- **Common problems:** 
  - Merge Intervals
  - Insert Interval
  - Meeting Rooms

---

## 🟧 Sliding Window Pattern

### 🔹 [Longest Substring Without Repeating Characters](./python/longestSubstringWithoutRepeatingCharacters.py)
- **When to use:** You need to find the longest or shortest subarray/string that satisfies a condition.
- **Key idea:** Expand the window to include valid elements; shrink when invalid.
- **Common problems:** 
  - Longest Substring Without Repeating Characters
  - Longest Subarray with K Distinct
  - Max Consecutive Ones III

### 🔹 [Minimum Window Substring](./python/minimumWindowSubstring.py)
- **When to use:** You need a minimal range that contains all required elements.
- **Key idea:** Maintain a frequency map, expand and shrink dynamically.
- **Common problems:** 
  - Minimum Window Substring
  - Find All Anagrams in a String
  - Substring with Concatenation of All Words

### [Sort Colors (Dutch flag partition)](./python/sortColors.py)
- **When to use:** When you need to sort a list based on three macro groups in place
- **Key idea:** We keep three separated partition and we traverse the middle one. We move the values in the middle partition in the left or right partition based on the macro group.

---

## 🟥 Heap Pattern

### 🔹 [Top K Frequent Elements](./python/topKFrequentElements.py)
- **When to use:** You need the largest/smallest K elements efficiently.
- **Key idea:** Maintain a min-heap of size K to discard the least relevant elements as you go.
- **Common problems:** 
  - Top K Frequent Elements
  - Kth Largest Element in an Array
  - Merge K Sorted Lists

### [Kth Largets Element in an Array](./python/kthLargestElementInAnArray.py)
- **When to use:** You need the top most k element efficiently like if you need the third max element for example
- **Key idea:** maintain a min-heap of size K to discard the least relevant elements as you go and return the first element of the heap when the algo looped over the list once

### [Merge K Sorted Lists](./python/mergeKSortedLists.py)
- **When to use:** You need to merge ordered linked lists
- **Key idea:** maintain a min-heap of size K pushing the first node of the each linked list only in the heap. While there are still nodes in the the heap, we pop one and we append it to the previous one, then if the node has a next node, we push that node in the heap too. We return the newly created linked list.

---

## 🧩 Summary — Pattern Recognition Map

| Problem Type | Pattern | Data Structure | Mental Trigger |
|---------------|----------|----------------|----------------|
| Find pairs / complements | Hashmap | Dict | "Need O(1) lookup?" |
| Group items by signature | Hashmap | Dict of signatures | "Need to bucket anagrams?" |
| Validate nested structure | Stack | Stack | "Open/close elements?" |
| Merge or combine ranges | Sort + Merge | Array | "Overlapping intervals?" |
| Find longest/shortest subarray | Sliding Window | HashMap / Set | "Contiguous segment constraint?" |
| Cover all required tokens | Sliding Window | HashMap + Counter | "Need smallest window covering target?" |
| In-place three-way partition | Dutch National Flag | Array + pointers | "Need to reorder three categories?" |
| Get top or smallest K elements | Heap | Min/Max Heap | "Top / frequent / ranked?" |
| Merge multiple sorted sources | Heap | Min Heap | "Need to merge many sorted feeds?" |
