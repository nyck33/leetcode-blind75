'''
207. Course Schedule
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''
from typing import List
class Solution_chatgpt:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create graph
        graph = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            graph[src].append(dest)

        # State arrays
        visited = [False] * numCourses

        # Helper function to perform iterative DFS
        def dfs_iterative(start):
            stack = [(start, 0)]  # (current node, current neighbor index)
            path = set()  # Set to track the current path

            while stack:
                current, index = stack[-1]
                if current not in path:
                    path.add(current)
                    visited[current] = True

                # If all neighbors are visited, pop from stack and continue
                if index == len(graph[current]):
                    path.remove(current)
                    stack.pop()
                    continue

                neighbor = graph[current][index]
                # Increment neighbor index in stack
                stack[-1] = (current, index + 1)

                # If neighbor is in the path, it's a cycle
                if neighbor in path:
                    return True
                # If neighbor has not been visited, push to stack
                if not visited[neighbor]:
                    stack.append((neighbor, 0))

            return False

        # Check for cycles in each component
        for course in range(numCourses):
            if not visited[course]:
                if dfs_iterative(course):
                    return False
        return True

from collections import deque
class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        ans = []

        for pair in prerequisites:
            course = pair[0]
            prerequisite = pair[1]
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()
            ans.append(current)

            for next_course in adj[current]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return len(ans) == n

# Example usage
if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    #print(Solution().canFinish(numCourses, prerequisites))  
    numCourses = 4
    prerequisites = [[1, 0], [2, 1], [3, 2]]
    print(Solution().canFinish(numCourses, prerequisites))
