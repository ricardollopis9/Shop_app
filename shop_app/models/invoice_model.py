from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class InvoiceModel(models.Model):
    _name = 'shop_app.invoice_model'
    _description = 'Invoice Model'
    _sql_constraints = [('invoice_unique_ref', 'UNIQUE (reference)', 'Reference must be unique!!')]

    reference = fields.Integer(string="Reference", readonly=True, required=True, index=True, help="Invoice Reference")
    date = fields.Date(string="Date", default=datetime.now(), help="Date")
    base = fields.Float(string="Base", default=0, help="Base Price", compute='_check_base', store=True)
    vat = fields.Selection(string="VAT", selection=[('0','0'), ('4','4'), ('10','10'), ('21','21')], default='21' ,help="This is the invoice VAT")
    total = fields.Float(string="Total", default=0, help="This final price", compute='_check_total', store=True)
    state = fields.Selection(selection=[('Draft','Draft'),('Confirmed','Confirmed')], default="Draft")

    lines_ids = fields.One2many("shop_app.line_model", "invoice_id", string="Invoice", required=True)
    client_id = fields.Many2one("shop_app.client_model", string="Client", required=True)
    employe_id = fields.Many2one("shop_app.employe_model", string="Attended by", required=True)

    @api.depends("lines_ids")
    def _check_base(self):
        sum = 0
        for line in self.lines_ids:
            sum += line.product_id.price * line.quantity
        
        self.base = sum
        return True

    @api.depends("base", "vat")
    def _check_total(self):
        self.total = self.base * int(self.vat) / 100 + self.base
        return True

    @api.model
    def create(self, vals):
        vals['reference'] = self.env['ir.sequence'].next_by_code('reference.test')
        return super(InvoiceModel, self).create(vals)

    def change_state(self):
        self.state = "Confirmed"
        self.ensure_one()
        self._cr.autocommit(False)

        if self.client_id.money >= self.total:
            self.client_id.money -= self.total
            for rec in self.lines_ids:
                if rec.quantity <= rec.product_id.stock:
                    rec.product_id.stock -= rec.quantity
                else:
                    self._cr.rollback()
                    self._cr.autocommit(True)
                    raise ValidationError("No hay suficiente stock.")
            self._cr.commit()
            self._cr.autocommit(True)
            return True
        else:
            raise ValidationError("El Cliente no tiene suficiente dinero para pagar o Cliente no seleccionados.")