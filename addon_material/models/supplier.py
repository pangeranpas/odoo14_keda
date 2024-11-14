from odoo import models, fields

class Supplier(models.Model):
    _name = 'supplier.supplier'
    _description = 'Supplier'

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    is_supplier = fields.Boolean(string="Supplier", default=True)
    rating = fields.Integer(string="Rating")
