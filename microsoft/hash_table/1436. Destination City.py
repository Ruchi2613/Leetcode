class Solution:
    def destCity(self, paths):
        graph = {}
        for a, b in paths:
            if b not in graph:
               graph[b] = []
            if a not in graph:
               graph[a] = []
            graph[a].append(b)


       
        for k, v in graph.items():
           if v == []:
               return k
