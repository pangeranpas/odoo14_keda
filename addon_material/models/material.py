from odoo import models, fields, api, exceptions

class Material(models.Model):
    _name = 'material.material'
    _description = 'Material for Sale'

    material_code = fields.Char(string="Material Code", required=True)
    material_name = fields.Char(string="Material Name", required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string="Material Type", required=True)
    material_buy_price = fields.Float(string="Material Buy Price", required=True)
    supplier_id = fields.Many2one('supplier.supplier', string="Related Supplier", required=True, domain="[('is_supplier', '=', True)]")

    @api.constrains('material_buy_price')
    def _check_material_buy_price(self):
        for record in self:
            if record.material_buy_price < 100:
                raise exceptions.ValidationError("Harga Material harus lebih besar atau sama dengan 100.")

