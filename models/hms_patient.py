from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date

class HmsPatient(models.Model):
    _name = 'hms.patient'
    _description = 'HMS Patient'
    _rec_name = 'first_name'
    _order = 'first_name'
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    email= fields.Char(string="Email", required=True)
    address = fields.Text(string="Address")
    history = fields.Html(string="History")
    age=fields.Integer(string="Age",compute="_compute_age",store=True)
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
    status=fields.Selection([
        ("undetermined", "Undetermined"),
        ("fine", "Fine"),
        ("good","Good"),
        ("serious","Serious")
    ],string="Status")
    department_id = fields.Many2one(
        "hms.department",
        string="Department"
    )

    doctor_ids = fields.Many2many(
        "hms.doctor",
        string="Doctors"
    )

    department_capacity = fields.Integer(
        related="department_id.capacity",
        readonly=True,
        store=True
    )

    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            if record.birth_date:
               record.age = date.today().year-record.birth_date.year
            else:
                record.age = 1


    @api.constrains("email")
    def _check_email(self):
        for record in self:
          if "@" not in record.email or "." not in record.email.split("@")[-1]:
             raise ValidationError("Email address is invalid")

    @api.constrains("pcr", "cr_ratio")
    def _mandatory_cr_ratio(self):
        for record in self:
            if record.pcr and not record.cr_ratio:
                raise ValidationError("u can't have pcr without cr_ratio")

    @api.onchange("age")
    def _mandatory_pcr(self):
            if self.age and self.age<30 and not self.pcr:
                self.pcr = True
                return{"warning":{"title":"pcr checked","message":"PCR is automatically checked because the age is less than 30"}}

    def status_action_undetermined(self):
        for record in self:
           record.status = "undetermined"
    def status_action_fine(self):
        for record in self:
            record.status = "fine"

    def status_action_good(self):
        for record in self:
            record.status = "good"

    def status_action_serious(self):
        for record in self:
            record.status = "serious"



