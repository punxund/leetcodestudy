#https://leetcode.com/problems/keys-and-rooms/description/
#2022-11-27 Hongsik Kim

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # using dfs and memoization, check which room is opened.
        visited_room = [False]*len(rooms) 
        def dfs(rooms, key, visited):
            visited_room[key] = True
            for i in rooms[key]:
                if visited_room[i] == False:
                    dfs(rooms, i, visited_room)
        
        dfs(rooms, 0, visited_room) # O(n)

        # if all rooms are opened, return True.
        for check in visited_room: # O(n)
            if check == False:
                return False
        return True