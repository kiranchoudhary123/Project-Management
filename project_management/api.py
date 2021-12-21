import frappe
from frappe import _


@frappe.whitelist()
def send_information_emails(project_task):
	project_task = frappe.get_doc("Project Task", project_task)
	project_task.check_permission("email")

	if project_task.status == "New":
		frappe.sendmail(
			recipients=[d.users for d in project_task.users],
			sender=frappe.session.user,
			subject=project_task.task_title,
			message=project_task.information_message,
			reference_doctype=project_task.doctype,
			reference_name=project_task.name
			
		)

		project_task.status = "Information Sent"
		project_task.save()

		frappe.msgprint(_("Information Sent"))

	else:
		frappe.msgprint(_("Project Task  Status must be 'New'"))
