from collections import defaultdict
import heapq 
n = 5
edges =  [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
dt = 4

def findTheCity(n, edges, dt):
    adj = defaultdict(list)
    for v1, v2, dist in edges:
        adj[v1].append((v2, dist))
        adj[v2].append((v1, dist))
    # print(adj)

    def dijkstra(src):
        heap = [(0, src)] # dist node
        visit = set()

        while heap:
            dist , node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            for nei, dist2 in adj[node]:
                nei_dist = dist + dist2
                if nei_dist <= dt:
                    heapq.heappush(heap, (nei_dist, nei))


        return len(visit) - 1

    res, min_count = -1, n
    for src in range(n):
        count = dijkstra(src)
        if count <= src:
            res, min_count = src, count
    return res




# class Solution:
#     def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
#         adj = {i:dict() for i in range(n)}
#         for u, v, d in edges:
#             if d <= distanceThreshold:
#                 adj[u][v] = d
#                 adj[v][u] = d
        
#         cities = [0] * n
#         for i in range(n):
#             count = -1

#             distance = [float('inf')] * n
#             distance[i] = 0
#             visited = [False] * n

#             pq = [(0, i)]
#             heapify(pq)

#             while pq:
#                 d, node = heappop(pq)
#                 if d > distanceThreshold:
#                     break
#                 if visited[node]:
#                     continue
#                 visited[node] = True
#                 count += 1
#                 for v in adj[node]:
#                     if not visited[v] and d + adj[node][v] < distance[v]:
#                         distance[v] = d + adj[node][v]
#                         heappush(pq, (distance[v], v))
#             cities[i] = count

#         max_node = 0
#         min_distnace = cities[0]
#         for i in range(n):
#             if cities[i] <= min_distnace:
#                 max_node = i
#                 min_distnace = cities[i]
#         return max_node