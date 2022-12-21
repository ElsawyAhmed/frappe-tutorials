# Copyright (c) 2022, Advintic and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	exams = frappe.get_all('Course', fields=['*'])
	print("Exams", exams)
	values = [[exam.get('name'), exam.get('level')] for exam in exams]
	print('==============\n', values)
	# enrolled_students = frappe.get_all('Enrolled Students', fields=['student', 'student_level', 'exam', 'grade'])
	# print("Enrolled_students", enrolled_students)
	columns, data = ['Student', 'Level', 'Exam', 'Grade'], []
	return columns, data
