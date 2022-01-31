from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductModel(models.Model):
    _name = 'shop_app.product_model'
    _description = 'Product Model'
    _sql_constraints = [('product_unique_name', 'UNIQUE (name)', 'Product Name must be Unique!!')]

    name = fields.Char(string="Name", required=True, index=True, help="Product Name")
    description = fields.Char(string="Description", index=True, help="Description")
    category = fields.Selection(string="Category", required=True, selection=[('Food','Food'), ('Movies','Movies'), ('Drinks','Drinks'), ('Furniture','Furniture'),('Clothing','Clothing'), ('Toys','Toys'), ('','')], default='' ,help="This is the products categories")
    price = fields.Float(string="Price", required=True, help="Price", default=0)
    vat = fields.Float(String="VAT", required=True, help="VAT", default=21)
    stock = fields.Integer(string='Stock', required=True, help="Product quantity", default = 0, store=True)

    @api.constrains("price")

    def _check_price(self):
        if(self.price > 0):
            return True
        else:
            raise ValidationError("Price can't be 0 or less than 0.")

    @api.constrains("stock")

    def _check_stock(self):
        if(self.stock >= 0):
            return True
        else:
            raise ValidationError("Quantity can't be 0 or less than 0.")

    @api.constrains("category")

    def check_category(self):
        if(self.category == ''):
            raise ValidationError("You must select a category for the product.")
        else:
            return True