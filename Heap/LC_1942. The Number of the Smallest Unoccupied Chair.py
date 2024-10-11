
'''
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.

 

Example 1:

Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1
Explanation: 
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.
Example 2:

Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2
Explanation: 
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.
 

Constraints:

n == times.length
2 <= n <= 104
times[i].length == 2
1 <= arrivali < leavingi <= 105
0 <= targetFriend <= n - 1
Each arrivali time is distinct.
'''

import heapq 

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        friends = [[friend_no, data[0], data[1]] for friend_no, data in enumerate(times)]
        friends.sort(key=lambda c: c[1])
        
        # Initialize a heap to manage the occupied chairs with (leaving time, chair number)
        heap = []
        # A min heap to manage available chairs
        available_chairs = []
        
        ch = 0  # This tracks the next available chair number if no free chairs exist
        
        for friend_no, s, e in friends:
            # Free up the chairs that have become available (leaving time <= arrival time)
            while heap and heap[0][0] <= s:
                prev_end, prev_ch = heapq.heappop(heap)
                heapq.heappush(available_chairs, prev_ch)
            
            # Allocate the smallest available chair or the next new one
            if available_chairs:
                expected_ch = heapq.heappop(available_chairs)
            else:
                expected_ch = ch
                ch += 1
            
            if friend_no == targetFriend:
                return expected_ch
            heapq.heappush(heap, [e, expected_ch])

