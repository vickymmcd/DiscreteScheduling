import sys
from students import sorted_conflicts as student_matrix
from students import total_course_conflicts
from instructors import sorted_conflicts as instructor_matrix

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
        if color not in self.conflicts:
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


schedule = Schedule(instructor_matrix, student_matrix, 8, 45)
res1 = schedule.get_coloring()
for i, val in enumerate(res1):
    print(total_course_conflicts[i][0], val)
