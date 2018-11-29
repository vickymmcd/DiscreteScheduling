import sys

class Schedule:
    def __init__(self, instructor_matrix, student_matrix, num_colors, num_classes):
        self.instructors = instructor_matrix
        self.students = student_matrix
        self.colors = []
        for i in range(0, num_colors):
            self.colors.append(i)
        self.num_classes = num_classes

    def get_coloring(self):
        self.result = []
        for i in range(0, self.num_classes):
            self.result.append(-1)

        #TODO (Vicky): Do this in order of descending conflict weight, sort first or something
        # consider the "name" of each vertex to be its index where the first one is 0
        def check_vertex(vertex):
            if vertex >= self.num_classes:
                return

            self.conflicts = {}
            for color in self.colors:
                if vertex >= self.num_classes:
                    return
                if (self.is_possible(vertex, color)):
                    self.conflicts = self.get_student_conflicts(vertex, color)

            least = sys.maxsize
            color = 0
            for key, val in self.conflicts.items():
                if val < least:
                    least = val
                    color = key
            self.result[vertex] = color
            check_vertex(vertex+1)
            return

        check_vertex(0)
        return self.result

    def get_student_conflicts(self, vertex, color):
        self.conflicts[color] = 0
        for v in range(0, self.num_classes):
            if(self.result[v] == color):
                self.conflicts[color] = self.conflicts[color] + self.students[v][vertex]
        return self.conflicts

    def is_possible(self, vertex, color):
        for v in range(0, self.num_classes):
            if (self.instructors[v][vertex] >= 1 and self.result[v] == color):
                return False
        return True


schedule = Schedule([[0,1,0],[1,0,0],[0,0,0]], [[0,1,0],[1,0,0],[0,0,0]], 3, 3)
res1 = schedule.get_coloring()
for val in res1:
    print(val)
