from odoo import fields, models,api
class HmsDepartment(models.Model):
    _name = 'hms.department'
    _description = 'HMS Department'
    name=fields.Selection([
        ("emergency","Emergency"),
        ("cardiology","Cardiology"),
        ("pedestrian","Pedestrian"),
        ("ent","ENT"),
        ("neurology","Neurology"),
    ],string="Department")
    patient_ids = fields.One2many(
        "hms.patient",
        "department_id",
        string="Patients"
    )

    doctor_ids = fields.One2many(
        "hms.doctor",
        "department_id",
        string="Doctors"
    )
    capacity = fields.Integer(string="Capacity")
    is_opened = fields.Boolean(string="Is Opened")
