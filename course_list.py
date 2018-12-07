import pandas
import numpy as np

students = pandas.read_csv('student_data.csv')

# Stores a dictionary of studentIDs and the courses they selected
student_dict = {}

# Stores the name of the course
student_course_list = []

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
    student_course_list = list(set(student_course_list).union(set(all_courses_no_empty)))


instructors = pandas.read_csv('2019courses.csv')

# Build a dictionary of instructors -> courses they teach
teaching_dict = {}
course_idx = {}
course_list = []

# Iterate through every offered course
for idx, course in instructors.iterrows():
    course_code = course['Course #']
    if course_code not in course_list: # Accounts for courses with multiple sections
        if course_code == 'MTH2188A / SCI2199A':
            course_code = 'MTH2188'
        if course_code == 'ENGR2199A':
            course_code = 'ENGR2199'
        if course_code == 'ENGR3299':
            course_code = 'ENGR3299A'
        course_idx[course_code] = idx
        course_list.append(course_code.replace(" ", ""))
        profs = course['Instructor'].split(';')
        for prof in profs:
            if prof != 'et al': # Ensure it's actually a professor
                if prof not in teaching_dict:
                    teaching_dict[prof] = [course_code]
                else:
                    teaching_dict[prof].append(course_code)

final_course_list = []
final_course_list = list(set(student_course_list).intersection(set(course_list)))
