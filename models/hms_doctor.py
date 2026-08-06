from odoo import fields, models,api
class hms_doctor(models.Model):
    _name = 'hms.doctor'
    _description = 'HMS Doctor'
    _rec_name = "first_name"
    first_name=fields.Char(string="First Name")
    last_name=fields.Char(string="Last Name")
    patient_ids=fields.One2many('hms.patient','department_id',string="Patients")
    capacity=fields.Integer(string="Capacity")
    is_opened=fields.Boolean(string="Is Opened")
    