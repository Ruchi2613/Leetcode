'''841. Keys and Rooms'''
from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited_room_track = set()
        q = deque()
        q.append(0)

        while len(q) > 0:

            room_key_address = q.popleft()

            if room_key_address in visited_room_track:
                continue
            else:
                visited_room_track.add(room_key_address)

            # to check how many keys are there inside room i.e;room_key_address
            for key in rooms[room_key_address]:
                if key not in visited_room_track:
                    q.append(key)

        return len(visited_room_track) == len(rooms)

''''''
