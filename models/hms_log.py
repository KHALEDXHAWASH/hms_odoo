from odoo import fields, models,api
class HMSLog(models.Model):
    _name = 'hms.log'
    _description = 'HMS Log'
    patient_id = fields.Many2one('hms.patient',string="Patient")
    created_at = fields.Datetime(string="Created at",related="patient_id.create_date")
    created_by = fields.Many2one("res.users",string="Created bu",related="patient_id.create_uid")
    history=fields.Html(string="Description")