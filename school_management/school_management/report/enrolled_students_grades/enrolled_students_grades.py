# Copyright (c) 2022, Advintic and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	exams = frappe.get_all('Exam Students', fields=['*'])
	print("Exams", exams)
	values = [[exam.get('exam'), exam.get('student'), exam.get('course'), exam.get('grade')] for exam in exams]
	print('==============\n', values)
	# enrolled_students = frappe.get_all('Enrolled Students', fields=['student', 'student_level', 'exam', 'grade'])
	# print("Enrolled_students", enrolled_students)
	columns, data = ['Exam', 'Student', 'Course', 'Grade'], values
	return columns, data
