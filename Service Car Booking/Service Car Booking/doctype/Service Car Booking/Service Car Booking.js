frappe.ui.form.on("Service Car Booking", {
	send_emails: function(frm) {
		if (frm.doc.status==="Planned") {
			frappe.call({
				method: "Service Car Booking.api.send_invitation_emails",
				args: {
					Service Car Booking: frm.doc.name
				}
			});
		}
	},
});

frappe.ui.form.on("Service Car Booking Attendee", {
	attendee: function(frm, cdt, cdn) {
		var attendee = frappe.model.get_doc(cdt, cdn);
		if (attendee.attendee) {
			// if attendee, get full name
			frappe.call({
				method: "Service Car Booking.Service Car Booking.doctype.Service Car Booking.Service Car Booking.get_full_name",
				args: {
					attendee: attendee.attendee
				},
				callback: function(r) {
					frappe.model.set_value(cdt, cdn, "full_name", r.message);
				}
			});

		} else {
			// if no attendee, clear full name
			frappe.model.set_value(cdt, cdn, "full_name", null);
		}
 	},
});

