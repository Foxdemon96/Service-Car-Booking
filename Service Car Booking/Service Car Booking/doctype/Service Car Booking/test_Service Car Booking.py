# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappé and Contributors
# See license.txt
from __future__ import unicode_literals

import frappe
import unittest

# test_records = frappe.get_test_records('Service Car Booking')

class TestService Car Booking(unittest.TestCase):
	def test_sync_todos_add(self):
		Service Car Booking = make_Service Car Booking()

		todos = get_todos(Service Car Booking)

		self.assertEquals(todos[0].name, Service Car Booking.minutes[0].todo)
		self.assertEquals(todos[0].description, Service Car Booking.minutes[0].description)


	def test_sync_todos_remove(self):
		Service Car Booking = make_Service Car Booking()

		Service Car Booking.minutes[0].status = "Closed"
		Service Car Booking.save()

		todos = get_todos(Service Car Booking)

		self.assertEquals(len(todos), 0)

	def test_sync_todos_on_close_todo(self):
		Service Car Booking = make_Service Car Booking()

		todos = get_todos(Service Car Booking)
		todo = frappe.get_doc("ToDo", todos[0].name)
		todo.status = "Closed"
		todo.save()

		Service Car Booking.reload()
		self.assertEquals(Service Car Booking.minutes[0].status, "Closed")
		self.assertFalse(Service Car Booking.minutes[0].todo)

	def test_sync_todos_on_delete_todo(self):
		Service Car Booking = make_Service Car Booking()

		todos = get_todos(Service Car Booking)
		todo = frappe.get_doc("ToDo", todos[0].name)
		todo.delete()

		Service Car Booking.reload()
		self.assertEquals(Service Car Booking.minutes[0].status, "Closed")
		self.assertFalse(Service Car Booking.minutes[0].todo)

def make_Service Car Booking():
	Service Car Booking = frappe.get_doc({
		"doctype": "Service Car Booking",
		"title": "Test Service Car Booking",
		"status": "Planned",
		"date": "2015-01-01",
		"from_time": "09:00",
		"to_time": "10:00",
		"minutes": [
			{
				"description": "Test Minute 1",
				"status": "Open",
				"assigned_to": "test@example.com"
			}
		]
	})
	Service Car Booking.insert()
	return Service Car Booking

def get_todos(Service Car Booking):
	return frappe.get_all("ToDo",
		filters={
			"reference_type": Service Car Booking.doctype,
			"reference_name": Service Car Booking.name,
			"owner": "test@example.com"
		},
		fields=["name", "description"])
