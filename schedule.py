def schedule(graph, colors):
    result = []
    colored = 0
    for i in range(0, len(graph[0])):
        result.append(-1)

    # consider the "name" of each vertex to be its index where the first one is 0
    def check_vertex(vertex, colored):
        if vertex >= len(graph[0]):
            return

        for color in colors:
            if vertex >= len(graph[0]):
                return
            print(vertex, color, colored)
            if (colored < len(graph[0]) and is_possible(vertex, color, graph, result)):
                result[vertex] = color
                colored+=1
                print("possible")
                vertex = vertex + 1
                check_vertex(vertex, colored)

    check_vertex(0, colored)
    return result


def is_possible(vertex, color, graph, result):
    for v in range(0, len(graph[0])):
        if (graph[v][vertex] >= 1 and result[v] == color):
                return False
    return True

res1 = schedule([[0,1,0],[1,0,0],[0,0,0]], [0,1,2])
for val in res1:
    print(val)
