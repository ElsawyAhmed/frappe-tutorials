# Copyright (c) 2022, Advintic and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Exam(Document):
	pass


@frappe.whitelist()
def send_mail(**kwargs):
	print("Hiiiiiiiii==============")
	print("args", kwargs)
	course = frappe.get_doc('Course', kwargs['course'])
	print("Course", course, course.enrolled_students)
	return True
