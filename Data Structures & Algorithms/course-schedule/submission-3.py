class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPre = {i: [] for i in range(numCourses)}
        visited = set()

        for c, p in prerequisites:
            courseToPre[c].append(p)

        def dfs(c):
            if c in visited:
                return False
            if courseToPre[c] == []:
                return True

            visited.add(c)

            for i in courseToPre[c]:
                if not dfs(i):
                    return False

            visited.remove(c)
            courseToPre[c] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


        