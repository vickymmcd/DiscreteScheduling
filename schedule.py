def schedule(graph, colors):
    result = []
    for i in range(0, len(graph[0])):
        result.append(-1)

    # consider the "name" of each vertex to be its index where the first one is 0
    def check_vertex(vertex):
        print(vertex)
        print(len(graph[0]))
        if vertex >= len(graph[0]):
            print("hiya!!")
            return
            print("this shouldn't happen")

        for color in colors:
            print(vertex, color)
            print("but this does??")
            if (is_possible(vertex, color, graph, result)):
                result[vertex] = color
                print("possible")
                vertex = vertex + 1
                check_vertex(vertex)

    check_vertex(0)
    return result


def is_possible(vertex, color, graph, result):
    for v in range(0, len(graph[0])):
        if (graph[v][vertex] >= 1 and result[v] == color):
                return False
    return True

res1 = schedule([[0,1,0],[1,0,0],[0,0,0]], [0,1,2])
for val in res1:
    print(val)
