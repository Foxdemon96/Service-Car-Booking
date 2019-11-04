frappe.views.calendar["Service Car Booking"] = {
	field_map: {
		"start": "start",
		"end": "end",
		"id": "name",
		"title": "title",
		"status": "status",
		"allDay": "all_day",
	},
	get_events_method: "Service Car Booking.api.get_Service Car Bookings"
}
