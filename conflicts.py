import sys
from students import sorted_conflicts as student_matrix
from students import total_course_conflicts, sorted_course_list, sorted_conflicts
from instructors import sorted_conflicts as instructor_matrix
from instructors import course_names
from schedule import Schedule

schedule = Schedule(instructor_matrix, student_matrix, 8, 45)
res1 = schedule.get_coloring()

per_sec = {}

for idx, section in enumerate(res1):
    if section not in per_sec:
        per_sec[section] = [idx]
    else:
        per_sec[section].append(idx)

for sec in per_sec.keys():
    all_classes = per_sec[sec]
    if len(all_classes) > 1:
        for i in range(len(all_classes)):
            for j in range(i+1, len(all_classes)):
                class1 = total_course_conflicts[all_classes[i]][0]
                class2 = total_course_conflicts[all_classes[j]][0]

                
                num_conflicts = sorted_conflicts[all_classes[i]][all_classes[j]]
                if num_conflicts > 1:
                    class1_name = total_course_conflicts[i][0]
                    class2_name = total_course_conflicts[j][0]
                    print("{} {} {}".format(course_names[class1_name], course_names[class2_name], str(num_conflicts)))