def get_edges(graph, alist):
    global cost
    global pos1
    global pos2

    status = True
    cost = 0
    pos1 = 0
    pos2 = 1

    def travel(graph, start, end):
        route = graph.graph[start]

        for city in route:

            if end == city.vertex:
                global cost
                cost += city.weight

                if end.value == alist[-1].value:
                    break
                else:
                    global pos1
                    pos1 += 1
                    global pos2
                    pos2 += 1
                    travel(graph, alist[pos1], alist[pos2])

    travel(graph, alist[pos1], alist[pos2])

    if cost == 0:
        status = False

    cost = f"${str(cost)}"
    return (status, cost,)
