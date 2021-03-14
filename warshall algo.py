
import sys
INF = sys.maxsize

def inputGraph():
    #graph = [[7,5,0,0],[7,0,0,2],[0,3,0,0],[4,0,1,0]]
    n = int(input("Enter number of vertices in the graph: "))
    graph = [[] for i in range(0,n)]
    for i in range(0,n):
        print("\nEnter weights of edges from vertex ",i+1," to every other vertex: \nNote: Enter zero if no edge joins two vertices.")
        for j in range(0,n):
            graph[i].append(int(input()))

    for i in range(0,n):
        for j in range(0,n):
            if graph[i][j] == 0:
                graph[i][j] = INF
    return graph

def floydWarshall(graph):
    # number of vertices in the graph
    n = len(graph)
    
    # dist will be the output matrix that will have the shortest distances between every pair of vertex.
    dist = [[] for i in range(n)]
    
    
    # Initialize the dist matrix as same as the input graph matrix.
    for i in range(n):
        for j in range(n):
            dist[i].append(graph[i][j])

    # Taking all vertices one by one and setting them as intermediate vertices
    for k in range(n):
        # Pick all vertices as source one by one.
        for i in range(n):
            # Pick all vertices as the destination for the above choosen source vertex.
            for j in range(n):
                # Update the value of dist[i][j] if k provides a shortest path from i to j
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

    # Shortest distance for every pair of vertex.
    print('Shortest Distance between every pair of vertex:-\n')
    for i in range(n):
        for j in range(n):
            if dist[i][j]==INF:
                print ("%5s" % ("INF"),end=' ')
            else:
                print ("%5s" % (dist[i][j]),end=' ')
        print()

#Driver Code
graph = inputGraph()
floydWarshall(graph)
