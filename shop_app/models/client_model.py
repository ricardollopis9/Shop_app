from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class ClientModel(models.Model):
    _name = 'shop_app.client_model'
    _description = 'Client Model'
    _sql_constraints = [('client_unique_dni','UNIQUE(DNI)','DNI must be unique!!')]

    name = fields.Char(string="Client Name", required=True, index=True, help="Client Name")
    surname = fields.Char(string="Surname", index=True, help="Surname")
    dni = fields.Char(string="DNI", size=9, required=True, help="Client DNI")
    phone = fields.Char(string="Phone", size=9, required=True, help="This is the client phone")
    photo = fields.Binary(string="Photo", help="This is a client photo")
    email = fields.Char(string="Email", required=True, help="This is the client email")
    money = fields.Float(string="Money", required=True, default=0, help="This is the client money")

    postalcode = fields.Char(string="Postal Code", required=True, index=True, help="Postal Code")
    city = fields.Char(string="City", required=True, index=True, help="City")
    direction = fields.Char(string="Direction", required=True, index=True, help="Direction")
    job = fields.Char(string="Job", index=True, help="job")

    invoices_ids = fields.One2many("shop_app.invoice_model", "client_id", string="Invoices")


    @api.constrains("dni")

    def _check_dni(self):
        dniList = "TRWAGMYFPDXBNJZSQVHLCKE"
        while True:
            if len(self.dni) == 9 and self.dni[:-1].isdigit and self.dni[-1].isalpha:
                decimals = int(self.dni[:-1]) % 23

                if self.dni[-1] == dniList[decimals]:
                    return True
                else:
                    raise ValidationError("Dni is not correct!")
            else:
                raise ValidationError("Dni is not correct!")

    @api.constrains("email")

    def _check_email(self):
        pEmail = '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.search(pEmail,self.email):

            raise ValidationError("Email is not correct!")

        return True