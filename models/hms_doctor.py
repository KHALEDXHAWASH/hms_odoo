from odoo import fields, models,api
class HmsDoctor(models.Model):
    _name = 'hms.doctor'
    _description = 'HMS Doctor'
    _rec_name = "first_name"
    first_name=fields.Char(string="First Name")
    last_name=fields.Char(string="Last Name")
    image=fields.Image(string="Image")
    ref=fields.Char(string="Ref",readonly=True,default="New")

    department_id = fields.Many2one(
        "hms.department",
        string="Department"
    )

    patient_ids = fields.Many2many(
        "hms.patient",
        string="Patients"
    )
    @api.model
    def create(self, vals):
        res=super(HmsDoctor,self).create(vals)
        if res.ref=="New":
            res.ref=self.env["ir.sequence"].next_by_code('doctor_sequence')
        return res
