class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        graph = defaultdict(list)

        for edges in prerequisites:
            graph[edges[0]].append(edges[1])
        
        def dfs(crs):

            # cycle 
            if crs in visited:
                return False
            # no prereqs
            if graph[crs] == []:
                return True
            
            visited.add(crs)
            for prereq in graph[crs]:
                if not dfs(prereq):
                    return False
            visited.remove(crs)
            graph[crs] = []

            return True

        for p in prerequisites:
            if not dfs(p[1]):
                return False
            
        return True