def dfs(graph, start, visited, stack):
    visited, stack = visited, stack
    visited.append(start)
    stack.append(start)
    print(start)
    for i in graph[start]:
        if not i in visited:
            dfs(graph, i, visited, stack)
                
s = int(input('Enter start node: '))
g=[]
v = int(input('No. of vertices: '))
print('\nEnter nodes: ')
n = [int(input()) for i in range(v)]
print('\nEnter end vertices: ')
e = [list(map(int, input().split())) for i in range(v)]
graph={n[i]:e[i] for i in range(0,v)}
print(f'\nGraph: {graph}')
print('\nDFS traversal: ')
dfs(graph, s, visited=[], stack=[])


'''
OUTPUT:

Enter start node: 2
No. of vertices: 6

Enter nodes: 
0
1
2
3
4
5

Enter end vertices: 
1 2 3
0 3 4
0 4 5
2 4 5
5
1

Graph: {0: [1, 2, 3], 1: [0, 3, 4], 2: [0, 4, 5], 3: [2, 4, 5], 4: [5], 5: [1]}

DFS traversal: 
2
0
1
3
4
5