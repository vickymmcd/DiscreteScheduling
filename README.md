# Olin Course Scheduling Using Graph Coloring

## Project Overview

In this project, we used graph coloring to optimize the Olin College course schedule. Our goal was to schedule class meeting times such that the largest number of students can take the classes they are interested in. This project involved data analysis of student and instructor conflicts as well as implementation of a graph coloring algorithm in Python.

## How to Use

To use our scheduling program, one should fill in the student and instructor data in the student_data.csv and instructor_data.csv files in this repository.

In instructor_data.csv, fill out course code, course description, and instructor name in the appropriate columns for each course being offered. If more than one instructor is teaching the same course, put all their names in the same cell in the spreadsheet and separate their names with semicolons.

In student_data.csv, fill in one row for each student, marking down their major, their graduation year, a unique ID, and the 5 courses they are most interested in taking (labeled C1 through C5 in the spreadsheet). Courses should be labeled in this spreadsheet using the same course code that was used in the instructor spreadsheet.

Then to run the algorithm and get a scheduling of all the classes into 8 blocks simply run the following in a terminal:
```
python3 schedule.py
```

## Supplemental Information

[Overview and Relevant Proofs](https://drive.google.com/file/d/1IFwiP55zrsmZ2LNjYHzkjQkYrvNgvXeD/view?usp=sharing)

[Final Presentation](https://docs.google.com/presentation/d/1udd0V4KmQUTm4z0gyqxA2X1Wi7JObEW7RzfqEL2WZ0Q/edit?usp=sharing)
