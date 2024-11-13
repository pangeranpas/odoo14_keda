from odoo import http
from odoo.http import request, Response

class MaterialController(http.Controller):

    @http.route('/api/materials', type='json', auth='user', methods=['GET'])
    def get_materials(self):
        materials = request.env['material.material'].search([])
        result = [{'material_code': m.material_code, 'material_name': m.material_name,
                   'material_type': m.material_type, 'material_buy_price': m.material_buy_price,
                   'supplier_id': m.supplier_id.name} for m in materials]
        return result

    @http.route('/api/materials', type='json', auth='user', methods=['POST'])
    def create_material(self, **kwargs):
        required_fields = ['material_code', 'material_name', 'material_type', 'material_buy_price', 'supplier_id']
        if not all(field in kwargs for field in required_fields):
            return Response("Missing required fields", status=400)

        supplier = request.env['res.partner'].browse(kwargs['supplier_id'])
        if not supplier or not supplier.supplier:
            return Response("Invalid supplier", status=400)

        material = request.env['material.material'].create({
            'material_code': kwargs['material_code'],
            'material_name': kwargs['material_name'],
            'material_type': kwargs['material_type'],
            'material_buy_price': kwargs['material_buy_price'],
            'supplier_id': kwargs['supplier_id'],
        })
        return material.id

    @http.route('/api/materials/<int:material_id>', type='json', auth='user', methods=['PUT'])
    def update_material(self, material_id, **kwargs):
        material = request.env['material.material'].browse(material_id)
        if not material.exists():
            return Response("Material not found", status=404)
        material.write(kwargs)
        return material.id

    @http.route('/api/materials/<int:material_id>', type='json', auth='user', methods=['DELETE'])
    def delete_material(self, material_id):
        material = request.env['material.material'].browse(material_id)
        if not material.exists():
            return Response("Material not found", status=404)
        material.unlink()
        return Response("Material deleted", status=200)
