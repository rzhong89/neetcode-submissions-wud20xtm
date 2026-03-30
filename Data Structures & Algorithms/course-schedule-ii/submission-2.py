class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = []
        visited = set()
        completed = set()
        preMap = defaultdict(list)

        for a, b in prerequisites:
            preMap[a].append(b)

        def dfs(crs):
            if crs in visited:
                return False

            if crs in completed:
                return True
            
            visited.add(crs)

            for p in preMap[crs]:
                if not dfs(p):
                    return False

            visited.remove(crs)
            completed.add(crs)
            path.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return path
