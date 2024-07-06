'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
'''
from typing import List
# Define a class Solution
'''
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
'''
class Solution:
    # Define a method insert that takes in intervals (a list of lists) and newInterval (a list)
    # and returns a list of lists
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Create an empty list to store the merged intervals
        merged = []
        # Initialize a variable i to 0
        i = 0

        # Iterate through the intervals until we find an interval whose end is less than the start of newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            # Append the current interval to the merged list if it doesn't overlap with newInterval
            merged.append(intervals[i])
            # Increment i
            i += 1
        
        # Iterate through the intervals while intervals' start is less than or equal to the end of newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            # Update newInterval to merge it with the current interval
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            # Increment i
            i += 1
        # Append the merged newInterval to the merged list
        merged.append(newInterval)
        
        # Append the remaining intervals to the merged list
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        
        # Return the merged list of intervals
        return merged