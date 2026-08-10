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
    user_id = fields.Many2one(
        "res.users",
        string="Responsible User",
        default=lambda self: self.env.user,
        store=True
    )
    #test=fields.Boolean(string="Test")
    email= fields.Char(string="Email", required=True)
    address = fields.Text(string="Address")
    history = fields.Html(string="History")
    age=fields.Integer(string="Age",compute="_compute_age",store=True)
    cr_ratio=fields.Float(string="Cr Ratio")
    birth_date = fields.Date(string="Birth Date")
    pcr=fields.Boolean(string="PCR")
    image=fields.Image(string="Image")
    #related_patient_id=fields.Many2one("res.partner",string="Related Patient")
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
    log_ids = fields.One2many(
        "hms.log",
        "patient_id",
        string="History Logs"
    )

    _unique_email = models.Constraint("UNIQUE (email)",
                                      "please enter a unique email address")

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

    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            if record.birth_date:
               record.age = date.today().year-record.birth_date.year

    @api.onchange("age")
    def _mandatory_pcr(self):
            if self.age and self.age<30 and not self.pcr:
                self.pcr = True
                return{"warning":{"title":"pcr checked","message":"PCR is automatically checked because the age is less than 30"}}

    @api.model_create_multi
    def create(self, vals_list):
        patients = super().create(vals_list)

        for patient in patients:
            self.env["hms.log"].create({
                "patient_id": patient.id,
                "history": "Patient created"
            })

        return patients

    def _create_status_log(self, status):
        self.env["hms.log"].create({
            "patient_id": self.id,
            "history": f"State changed to {status}"
        })
    def status_action_undetermined(self):
        for record in self:
            record.status = "undetermined"
            record._create_status_log("Undetermined")

    def status_action_fine(self):
        for record in self:
            record.status = "fine"
            record._create_status_log("Fine")

    def status_action_good(self):
        for record in self:
            record.status = "good"
            record._create_status_log("Good")

    def status_action_serious(self):
        for record in self:
            record.status = "serious"
            record._create_status_log("Serious")

