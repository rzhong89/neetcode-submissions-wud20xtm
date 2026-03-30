class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = defaultdict(list)
        visited = set()
        path = set()
        res = []

        for a, b in prerequisites:
            preMap[a].append(b)

        def dfs(i):
            if i in path:
                return False
            if i in visited:
                return True
            
            path.add(i)

            for nei in preMap[i]:
                if not dfs(nei):
                    return False
            
            path.remove(i)
            visited.add(i)
            res.append(i)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        return res