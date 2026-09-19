class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            graph[crs].append(pre)
        
        res = []
        visited = set()
        visiting = set()

        def dfs(course):
            
            if course in visiting:
                return False
            
            if course in visited:
                return True
            
            visiting.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for p in range(numCourses):
            if not dfs(p):
                return []
        return res