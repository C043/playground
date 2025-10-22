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

---

## 🟥 Heap Pattern

### 🔹 [Top K Frequent Elements](./python/topKFrequentElements.py)
- **When to use:** You need the largest/smallest K elements efficiently.
- **Key idea:** Maintain a min-heap of size K to discard the least relevant elements as you go.
- **Common problems:** 
  - Top K Frequent Elements
  - Kth Largest Element in an Array
  - Merge K Sorted Lists

---

## 🧩 Summary — Pattern Recognition Map

| Problem Type | Pattern | Data Structure | Mental Trigger |
|---------------|----------|----------------|----------------|
| Find pairs / complements | Hashmap | Dict | "Need O(1) lookup?" |
| Validate nested structure | Stack | Stack | "Open/close elements?" |
| Merge or combine ranges | Sort + Merge | Array | "Overlapping intervals?" |
| Find longest/shortest subarray | Sliding Window | HashMap / Set | "Contiguous segment constraint?" |
| Get top or smallest K elements | Heap | Min/Max Heap | "Top / frequent / ranked?" |

