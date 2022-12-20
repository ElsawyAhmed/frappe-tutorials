# Copyright (c) 2022, Advintic and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Course(Document):
	def before_save(self):
		for student in self.enrolled_students:
			if student.student_level != self.level:
				frappe.throw(f"The Student {student.student} Level Should be the same as the course level")
