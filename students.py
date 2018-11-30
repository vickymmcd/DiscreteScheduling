import pandas
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

students = pandas.read_csv('Course Fair Survey Data_for_SP19.csv')

# Stores a dictionary of studentIDs and the courses they selected
student_dict = {}

# Stores the name of the course
course_list = []

# Iterate through every student
for idx, student in students.iterrows():
    # Get the unique student id
    student_id = student['Unique ID']

    # Each student has chosen up to 5 classes to select
    # Extract the course code from the class name
    course_code1 = str(student['C1']).split()[0][:-1]
    course_code2 = str(student['C2']).split()[0][:-1]
    course_code3 = str(student['C3']).split()[0][:-1]
    course_code4 = str(student['C4']).split()[0][:-1]
    course_code5 = str(student['C5']).split()[0][:-1]

    # Construct the list of all 5 chosen courses
    all_courses = [course_code1, course_code2, course_code3, course_code4, course_code5]

    # Get rid of any na courses where people didn't fill out the box
    all_courses_no_empty = list(filter(lambda name: name != "na", all_courses))

    # Add the student and chosen classes to the dictionary
    student_dict[student_id] = all_courses_no_empty

    # Add the courses to the course_list if they are not there already
    course_list = list(set(course_list).union(set(all_courses_no_empty)))

print(course_list)

# Order the course list in alphabetical order
#course_list = sorted(course_list)

# The adjacency matrix, with courses as vertices and edges indicating two classes were chosen by the same student
conflicts = np.zeros((len(course_list), len(course_list)))

# For each student, if they want multiple courses, mark those points in the adjacency matrix
for student in student_dict:
    if len(student_dict[student]) > 1:
        classes_wanted = student_dict[student]

        # Get each unique pair of (different) courses taught
        for i in range(len(classes_wanted)):
            for j in range (i+1, len(classes_wanted)):
                # Get the name of the class that is wanted
                class1 = classes_wanted[i]
                class2 = classes_wanted[j]

                # Using the indices of the classes in course_list, update adjacency value
                conflicts[course_list.index(class1)][course_list.index(class2)] += 1
                conflicts[course_list.index(class2)][course_list.index(class1)] += 1
print(conflicts)

# Find the sum of the conflicts for each class by summing the row values
summation = np.sum(conflicts,axis=1)

# Stores a dictionary relating the course and the total conflicts
total_course_conflicts = []

# For each course, add a dictionary with the course id and the conflict summation
for idx, course in enumerate(course_list):
    total_course_conflicts.append((course,summation[idx]))

total_course_conflicts.sort(key=lambda x:x[1], reverse=True)
print(total_course_conflicts)

# Stores the sorted adjacency matrix
sorted_conflicts = []#np.zeros((len(course_list), len(course_list)))

# For each row in the ordered total_course_conflicts, put that row into a new ordered matrix
for name,num in total_course_conflicts:
    # Stores the row for the class in the unordered matrix
    original_row = course_list.index(name)

    # Add the row to the ordered position
    sorted_conflicts.append(conflicts[original_row].tolist())

print(sorted_conflicts)
