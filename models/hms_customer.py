from odoo import api,fields,models
from odoo.exceptions import ValidationError
class HmsCustomer(models.Model):
    _inherit = "res.partner"
    related_patient_id=fields.Many2one("hms.patient",string="Related Patient")
    vat = fields.Char(string="Tax ID", required=True)
    def unlink(self):
        for record in self:
            if record.related_patient_id:
                raise ValidationError(
                    "You cannot delete a customer linked to a patient."
                )
        return super().unlink()

    @api.constrains("email")
    def _check_email(self):
        for record in self:
          patients=self.env["hms.patient"].search([("email","=",record.email)])
          if patients:
            raise ValidationError("Email already exists")

