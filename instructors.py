import pandas
import numpy as np
from course_list import final_course_list
from students import total_course_conflicts

instructors = pandas.read_csv('2019courses.csv')

# Build a dictionary of instructors -> courses they teach
teaching_dict = {}
course_idx = {}
course_list = []

count = 0
# Iterate through every offered course
for idx, course in instructors.iterrows():
    course_code = course['Course #']
    if course_code == 'MTH2188A / SCI2199A':
        course_code = 'MTH2188'
    if course_code == 'ENGR2199A':
        course_code = 'ENGR2199'
    if course_code == 'ENGR3299':
        course_code = 'ENGR3299A'
    course_code = course_code.replace(" ", "")
    if course_code not in course_list and course_code in final_course_list: # Accounts for courses with multiple sections
        course_idx[course_code] = count
        count+=1
        course_list.append(course_code)
        profs = course['Instructor'].split(';')
        for prof in profs:
            if prof != 'et al': # Ensure it's actually a professor
                if prof not in teaching_dict:
                    teaching_dict[prof] = [course_code]
                else:
                    teaching_dict[prof].append(course_code)

# The adjacency matrix, with courses as vertices and edges indicating two classes taught by the same professor
conflicts = np.zeros((len(course_list), len(course_list)))


# For each professor, if they teach multiple courses, mark those points in the adjacency matrix
for prof in teaching_dict:
    if len(teaching_dict[prof]) > 1:
        classes_taught = teaching_dict[prof]
        # Get each unique pair of (different) courses taught
        for i in range(len(classes_taught)):
            for j in range (i+1, len(classes_taught)):
                class1 = classes_taught[i]
                class2 = classes_taught[j]

                conflicts[course_idx[class1]][course_idx[class2]] = 1
                conflicts[course_idx[class2]][course_idx[class1]] = 1

# Stores the sorted adjacency matrix
sorted_conflicts = []#np.zeros((len(course_list), len(course_list)))

# For each row in the ordered total_course_conflicts, put that row into a new ordered matrix
for name,num in total_course_conflicts:
    # Stores the row for the class in the unordered matrix
    original_row = course_idx[name]

    # Add the row to the ordered position
    sorted_conflicts.append(conflicts[original_row].tolist())

sorted_course_list = []
for name,num in total_course_conflicts:
    sorted_course_list.append(name)

for i, name in enumerate(sorted_course_list):
    # Stores the row for the class in the unordered matrix
    original_idx = course_idx[name]
    for j, val in enumerate(conflicts[original_idx].tolist()):
        class2 = course_list[j]
        sorted_conflicts[i][sorted_course_list.index(class2)] = conflicts[original_idx][j]
