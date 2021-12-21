// Copyright (c) 2021, kiran and contributors
// For license information, please see license.txt

frappe.ui.form.on('Project Task', {
	send_emails: function(frm) {
		if (frm.doc.status==="New") {
			frappe.call({
				method: "project_management.api.send_information_emails",
				args: {
					project_task: frm.doc.name
				}
			});
		}
	},
});


