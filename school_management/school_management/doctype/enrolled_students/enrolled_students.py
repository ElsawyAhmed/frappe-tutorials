# Copyright (c) 2022, Advintic and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class EnrolledStudents(Document):
	def before_save(self):
		print("Inside child", self.level, self.student)
