# Copyright (c) 2022, Advintic and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Teacher(Document):
	def before_save(self):
		self.full_name = self.first_name + ' ' + self.last_name
