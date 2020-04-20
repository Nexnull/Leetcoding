from heapq import *


class Solution(object):
    def travel(self, airports, departure, path):
        while airports[departure]:
            self.travel(airports, heappop(airports[departure]), path)
        path.append(departure)
        return path

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        airports = {}
        # priority queue -> smallest lexical order
        for ticket in tickets:
            if ticket[0] not in airports:
                airports[ticket[0]] = [ticket[1]]
            else:
                heappush(airports[ticket[0]], ticket[1])

            if ticket[1] not in airports:
                airports[ticket[1]] = []

        return self.travel(airports, "JFK", [])[::-1]

"""
https://algocasts.io/episodes/nwp8qrW7
答案：

"""