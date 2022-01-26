from itertools import product
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class LineModel(models.Model):
    _name = 'shop_app.line_model'
    _description = 'Line Model'

    invoice_id = fields.Many2one("shop_app.invoice_model", string="Invoice", help="Invoice Reference")
    product_id = fields.Many2one("shop_app.product_model", string="Product", help="Product Reference")

    quantity = fields.Integer(string="Quantity", required=True, index=True, help="Product Quantity")

    