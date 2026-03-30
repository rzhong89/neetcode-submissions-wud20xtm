class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visited = set()

        for a, b in prerequisites:
            preMap[a].append(b)

        def dfs(c):
            if c in visited:
                return False

            if preMap[c] == []:
                return True

            visited.add(c)
            
            for n in preMap[c]:
                if not dfs(n):
                    return False

            visited.remove(c)
            
            preMap[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True