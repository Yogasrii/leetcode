import heapq

class Solution:
    def getSkyline(self, buildings):
        events = []

        # Create start and end events
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        # Sort events by x-coordinate
        events.sort()

        result = []
        heap = [(0, float('inf'))]  # (negative height, end)

        i = 0

        while i < len(events):
            x = events[i][0]

            # Remove buildings that have ended
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            # Add all buildings starting at x
            while i < len(events) and events[i][0] == x:
                _, neg_height, right = events[i]

                if neg_height != 0:
                    heapq.heappush(heap, (neg_height, right))

                i += 1

            # Remove expired buildings again
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            current_height = -heap[0][0]

            # Add a key point only when height changes
            if not result or result[-1][1] != current_height:
                result.append([x, current_height])

        return result