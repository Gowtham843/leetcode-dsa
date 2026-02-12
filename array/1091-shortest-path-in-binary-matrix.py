"""
 1091. Shortest Path in Binary Matrix
 URL: https://leetcode.com/problems/shortest-path-in-binary-matrix/submissions/1917194887/
 Difficulty: Medium
 Topics: Array, Breadth-First Search, Matrix
 Date: 2026-02-12T17:00:55.557Z
"""

            r, c, dist = q.popleft()
            if r == row - 1 and c == col - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < row and
                    0 <= nc < col and
                    grid[nr][nc] == 0 and
                    (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))

        return -1

