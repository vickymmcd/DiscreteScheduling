import pandas
import numpy as np
import networkx as nx

instructors = pandas.read_csv('2019courses.csv')

# Build a dictionary of instructors -> courses they teach
teaching_dict = {}
course_idx = {}
course_list = []

# Iterate through every offered course
for idx, course in instructors.iterrows():
    course_code = course['Course #']
    if course_code not in course_list: # Accounts for courses with multiple sections
        course_idx[course_code] = idx
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
print(conflicts)
