#!/usr/bin/env python
# -*- coding: utf-8 -*-


from graph import MyGraph
from collections import deque


def BFS(graph, s):
    for v, a in graph.attributes.items():
        a['color'] = 'white'
        a['d'] = float('inf')
        a['pi'] = None

    q = deque()

    graph.attributes[s]['d'] = 0
    graph.attributes[s]['pi'] = None
    graph.attributes[s]['color'] = 'gray'
    q.append(s)
    print(graph.adj)
    step = 0
    while len(q) > 0:
        step += 1
        print(step, [graph.attributes[v]['name'] for v in q])
        print(step, [graph.attributes[v]['d'] for v in q])
        graph.draw('{}'.format(step))
        v = q.popleft()
        for j in graph.adj[v]:
            if graph.attributes[j]['color'] == 'white':
                q.append(j)
                graph.attributes[j]['d'] = int(graph.attributes[v]['d'])+1
                graph.attributes[j]['pi']=v
                graph.attributes[j]['color'] = 'gray'
        graph.attributes[v]['color'] = 'black'
    graph.draw('{}'.format(step))
def main():
    g = MyGraph()
    g.add_vertices(8)
    for i, c in enumerate(['r', 's', 't', 'u', 'v', 'w', 'x', 'y']):
        g.attributes[i]['name'] = c

    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 5)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(2, 3)
    g.add_edge(3, 6)
    g.add_edge(3, 7)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    BFS(g, 1)


if __name__ == "__main__":
    main()