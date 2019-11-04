import frappe
from frappe import _
from frappe.utils import nowdate, add_days

@frappe.whitelist()
def send_invitation_emails(Service Car Booking):
	Service Car Booking = frappe.get_doc("Service Car Booking", Service Car Booking)
	Service Car Booking.check_permission("email")

	if Service Car Booking.status == "Planned":
		frappe.sendmail(
			recipients=[d.attendee for d in Service Car Booking.attendees],
			sender=frappe.session.user,
			subject=Service Car Booking.title,
			message=Service Car Booking.invitation_message,
			reference_doctype=Service Car Booking.doctype,
			reference_name=Service Car Booking.name,
			as_bulk=True
		)

		Service Car Booking.status = "Invitation Sent"
		Service Car Booking.save()

		frappe.msgprint(_("Invitation Sent"))

	else:
		frappe.msgprint(_("Service Car Booking Status must be 'Planned'"))

@frappe.whitelist()
def get_Service Car Bookings(start, end):
	if not frappe.has_permission("Service Car Booking", "read"):
		raise frappe.PermissionError

	return frappe.db.sql("""select
		timestamp(`date`, from_time) as start,
		timestamp(`date`, to_time) as end,
		name,
		title,
		status,
		0 as all_day
	from `tabService Car Booking`
	where `date` between %(start)s and %(end)s""", {
		"start": start,
		"end": end
	}, as_dict=True)

def make_orientation_Service Car Booking(doc, method):
	"""Create an orientation Service Car Booking when a new User is added"""
	Service Car Booking = frappe.get_doc({
		"doctype": "Service Car Booking",
		"title": "Orientation for {0}".format(doc.first_name),
		"date": add_days(nowdate(), 1),
		"from_time": "09:00",
		"to_time": "09:30",
		"status": "Planned",
		"attendees": [{
			"attendee": doc.name
		}]
	})
	# the System Manager might not have permission to create a Service Car Booking
	Service Car Booking.flags.ignore_permissions = True
	Service Car Booking.insert()

	frappe.msgprint(_("Orientation Service Car Booking created"))

def update_minute_status(doc, method=None):
	"""Update minute status to Closed if ToDo is closed or deleted"""
	if doc.reference_type != "Service Car Booking" or doc.flags.from_Service Car Booking:
		return

	if method=="on_trash" or doc.status=="Closed":
		Service Car Booking = frappe.get_doc(doc.reference_type, doc.reference_name)
		for minute in Service Car Booking.minutes:
			if minute.todo == doc.name:
				minute.db_set("todo", None, update_modified=False)
				minute.db_set("status", "Closed", update_modified=False)
