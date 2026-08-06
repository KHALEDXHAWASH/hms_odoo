from odoo import fields, models,api
class hms_department(models.Model):
    _name = 'hms.department'
    _description = 'HMS Department'
    name=fields.Char(string="Name")
    patient_ids=fields.One2many('hms.patient','department_id',string="Patients")
    capacity=fields.Integer(string="Capacity")
    is_opened=fields.Boolean(string="Is Opened")
    