from odoo import fields, models,api
class HmsDoctor(models.Model):
    _name = 'hms.doctor'
    _description = 'HMS Doctor'
    _rec_name = "first_name"
    first_name=fields.Char(string="First Name")
    last_name=fields.Char(string="Last Name")
    image=fields.Image(string="Image")

    department_id = fields.Many2one(
        "hms.department",
        string="Department"
    )

    patient_ids = fields.Many2many(
        "hms.patient",
        string="Patients"
    )