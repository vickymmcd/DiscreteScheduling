import sys
from students import sorted_conflicts as student_matrix
from students import total_course_conflicts
from instructors import sorted_conflicts as instructor_matrix
from instructors import course_names

class Schedule:
    def __init__(self, instructor_matrix, student_matrix, num_colors, num_classes):
        self.instructors = instructor_matrix
        self.students = student_matrix
        self.colors = []
        for i in range(0, num_colors):
            self.colors.append(i)
        self.num_classes = num_classes
        self.conflict_sum = 0

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
            self.conflict_sum = self.conflict_sum + least
            self.result[vertex] = color
            check_vertex(vertex+1)
            return

        if len(self.instructors) > 0:
            check_vertex(0)
        print(self.conflict_sum)
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

print("Schedule:")
print()
print("Block #1")
for i, val in enumerate(res1):
    if val == 0:
        print(course_names[total_course_conflicts[i][0]])

print()
print("Block #2")
for i, val in enumerate(res1):
    if val == 1:
        print(course_names[total_course_conflicts[i][0]])

print()
print("Block #3")
for i, val in enumerate(res1):
    if val == 2:
        print(course_names[total_course_conflicts[i][0]])

print()
print("Block #4")
for i, val in enumerate(res1):
    if val == 3:
        print(course_names[total_course_conflicts[i][0]])

print()
print("Block #5")
for i, val in enumerate(res1):
    if val == 4:
        print(course_names[total_course_conflicts[i][0]])

print()
print("Block #6")
for i, val in enumerate(res1):
    if val == 5:
        print(course_names[total_course_conflicts[i][0]])

print()
print("Block #7")
for i, val in enumerate(res1):
    if val == 6:
        print(course_names[total_course_conflicts[i][0]])

print()
print("Block #8")
for i, val in enumerate(res1):
    if val == 7:
        print(course_names[total_course_conflicts[i][0]])
