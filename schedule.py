class Schedule:
    def __init__(self, instructor_matrix, student_matrix, colors, num_classes):
        self.instructors = instructor_matrix
        self.students = student_matrix
        self.colors = colors
        self.num_classes = num_classes

    def get_coloring(self):
        self.result = []
        colored = 0
        for i in range(0, self.num_classes):
            self.result.append(-1)

        #TODO (Vicky): Do this in order of descending conflict weight, sort first or something
        # consider the "name" of each vertex to be its index where the first one is 0
        def check_vertex(vertex, colored):
            if vertex >= self.num_classes:
                return

            for color in self.colors:
                if vertex >= self.num_classes:
                    return
                if (colored < self.num_classes and self.is_possible(vertex, color)):
                    self.result[vertex] = color
                    colored+=1
                    vertex = vertex + 1
                    check_vertex(vertex, colored)
                    return

        check_vertex(0, colored)
        return self.result

    def is_possible(self, vertex, color):
        for v in range(0, self.num_classes):
            if (self.instructors[v][vertex] >= 1 and self.result[v] == color):
                return False
            if (self.students[v][vertex] >= 3 and self.result[v] == color):
                return False
        return True


schedule = Schedule([[0,1,0],[1,0,0],[0,0,0]], [[0,1,0],[1,0,0],[0,0,0]], [0,1,2], 3)
res1 = schedule.get_coloring()
for val in res1:
    print(val)
