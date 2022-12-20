# Copyright (c) 2022, Advintic and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Exam(Document):
	pass


@frappe.whitelist()
def send_mail(**kwargs):
	print("args", kwargs)
	course = frappe.get_doc('Course', kwargs['course'])
	print("Course", course, course.enrolled_students)
	recipients = []
	for enrolled_student in course.enrolled_students:
		student = frappe.get_doc('Student', enrolled_student.student)
		print("student {} , mail {}".format(student, student.email))
		if student.email:
			recipients.append(student.email)
	if recipients:
		frappe.sendmail(
			recipients=recipients,
			subject=frappe._('Exam Appointment'),
			message=f"Dear {student.name},"
					f"\t Supposed You are enrolled in our course:{course.course_name},"
					f" you will have an exam at <b>{kwargs['appointment']}</b>"
					f"\n Best Regards:\n "
		)
	return True
