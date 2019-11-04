# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "Service Car Booking"
app_title = "Service Car Booking"
app_publisher = "Frappé"
app_description = "Prepare agenda, invite users and record minutes of a Service Car Booking"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@frappe.io"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/Service Car Booking/css/Service Car Booking.css"
# app_include_js = "/assets/Service Car Booking/js/Service Car Booking.js"

# include js, css files in header of web template
# web_include_css = "/assets/Service Car Booking/css/Service Car Booking.css"
# web_include_js = "/assets/Service Car Booking/js/Service Car Booking.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Service Car Booking"]

# Installation
# ------------

# before_install = "Service Car Booking.install.before_install"
# after_install = "Service Car Booking.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "Service Car Booking.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"User": {
		"after_insert": "Service Car Booking.api.make_orientation_Service Car Booking"
	},
	"ToDo": {
		"on_update": "Service Car Booking.api.update_minute_status",
		"on_trash": "Service Car Booking.api.update_minute_status"
	}
}

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"Service Car Booking.tasks.all"
# 	],
# 	"daily": [
# 		"Service Car Booking.tasks.daily"
# 	],
# 	"hourly": [
# 		"Service Car Booking.tasks.hourly"
# 	],
# 	"weekly": [
# 		"Service Car Booking.tasks.weekly"
# 	]
# 	"monthly": [
# 		"Service Car Booking.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "Service Car Booking.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "Service Car Booking.event.get_events"
# }

