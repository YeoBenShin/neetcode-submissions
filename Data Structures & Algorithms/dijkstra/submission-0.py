import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # initialise the start
        m_heap = []
        d_edges = dict()
        d_edges[src] = 0
        for edge in edges:
            if edge[0] == src: # start
                d_edges
                d_edges[edge[1]] = edge[2] # distance from src to edge[1]
                heapq.heappush(m_heap, (edge[2], edge[1]))

        while len(m_heap) != 0:
            dis, start = heapq.heappop(m_heap) # pop the min dis in the heap
            if d_edges.get(start) != dis: # old input
                continue
            for edge in edges:
                if edge[0] == start: # start
                    next_node = edge[1]
                    next_dis = edge[2]
                    if next_node in d_edges:
                        # compare to see if we found a new min
                        if d_edges.get(next_node) > dis + next_dis:
                            d_edges[next_node] = dis + next_dis
                            # update the heap
                            heapq.heappush(m_heap, (dis+next_dis, edge[1]))
                    else:
                        d_edges[next_node] = dis + next_dis
                        heapq.heappush(m_heap, (dis+next_dis, edge[1]))
        return d_edges
                    