class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visited = set()

        # construct preMap
        for a, b in prerequisites:
            preMap[a].append(b)

        def dfs(i):
            if i in visited:
                return False
            if preMap[i] == []:
                return True

            visited.add(i)
            
            for nei in preMap[i]:
                if not dfs(nei):
                    return False

            visited.remove(i)
            preMap[i] = []

            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
        