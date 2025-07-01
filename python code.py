from queue import PriorityQueue
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        # Initialize the skyline results array, a list to store building edges,
        # and a priority queue to manage the current highest buildings
        skyline = []
        edges = []
        max_heights = PriorityQueue()
      
        # Create a sorted list of all critical points (building start and end)
        for building in buildings:
            edges.extend([building[0], building[1]])
        edges.sort()
      
        # Initialize pointers and get the total number of buildings
        building_index, total_buildings = 0, len(buildings)

        # Process each edge in the sorted list to determine skyline changes
        for edge in edges:
            # Add buildings to the priority queue which start before or at the current edge
            while building_index < total_buildings and buildings[building_index][0] <= edge:
                # Insert into the priority queue the negative height (to reverse the default order),
                # the start, and the end of the current building
                max_heights.put([-buildings[building_index][2], buildings[building_index][1]])
                building_index += 1
          
            # Remove buildings from priority queue which end before the current edge
            while not max_heights.empty() and max_heights.queue[0][1] <= edge:
                max_heights.get()

            # The height is 0 if there are no buildings in sight, or the highest if there are
            height = -max_heights.queue[0][0] if not max_heights.empty() else 0
          
            # Only add a point to the skyline if the height changes from the last point
            if not skyline or skyline[-1][1] != height:
                skyline.append([edge, height])
      
        return skyline
