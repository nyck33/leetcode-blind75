'''
Problem Statement
Given a list of words sorted according to the lexicographical order of an alien language, derive the order of characters in that language.

Example
Input: words = ["wrt", "wrf", "er", "ett", "rftt"]

Output: "wertf"

Explanation:
From the given words list:

The order between w and e can be deduced since wrt comes before er.
From wrt and wrf, the order between t and f is established.
From er and ett, the order between r and t is known.
And so on...
Challenges
The ordering rules are not directly given but must be inferred from the sequence of words.
Not all letters are necessarily related directly or at all, leading to partial orders.
The graph that represents these partial orders might contain cycles, which would make ordering impossible (i.e., the input is invalid).
Approach to Solution
Graph Construction:
Each unique character in the alien language is a node in the graph.
Directed edges between nodes define the precedence constraints (e.g., a -> b if a must come before b).
Edge Deduction:
Compare adjacent words in the list to find the first differing character, establishing a directed edge from the first character to the second. This edge indicates the ordering.
Topological Sort:
Use topological sorting to determine the order of characters. This sort can be performed using:
Kahn's Algorithm (BFS approach)
DFS with recursion stack
'''