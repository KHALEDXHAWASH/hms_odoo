from odoo import api, fields, models
class HmsPatient(models.Model):
    _name = 'hms.patient'
    _description = 'HMS Patient'
    _rec_name = 'first_name'
    _order = 'first_name'
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    address = fields.Text(string="Address")
    history = fields.Html(string="History")
    age=fields.Integer(string="Age")
    cr_ratio=fields.Float(string="Cr Ratio")
    birth_date = fields.Date(string="Birth Date")
    pcr=fields.Boolean(string="PCR")
    image=fields.Image(string="Image")
    blood_type = fields.Selection([
        ("a+", "A+"),
        ("a-", "A-"),
        ("ab+", "AB+"),
        ("ab-", "AB-"),
        ("b+", "B+"),
        ("b-", "B-"),
        ("o+", "O+"),
        ("o-", "O-"),
    ], string="Blood Type")
    department_id=fields.Many2one("hms_patient",string="Department")