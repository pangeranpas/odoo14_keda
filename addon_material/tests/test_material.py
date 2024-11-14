from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestMaterial(TransactionCase):

    def setUp(self):
        super(TestMaterial, self).setUp()
        self.material_model = self.env['material.material']
        self.supplier = self.env['supplier.supplier'].create({
            'name': 'Test Supplier',
            'is_supplier': True,
        })

    def test_create_material(self):
        material = self.material_model.create({
            'material_code': 'MAT001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 150,
            'supplier_id': self.supplier.id,
        })
        self.assertEqual(material.material_code, 'MAT001')
        self.assertEqual(material.material_type, 'fabric')

    def test_material_buy_price_validation(self):
        with self.assertRaises(ValidationError):
            self.material_model.create({
                'material_code': 'MAT002',
                'material_name': 'Invalid Price Material',
                'material_type': 'cotton',
                'material_buy_price': 90,
                'supplier_id': self.supplier.id,
            })

    def test_update_material(self):
        material = self.material_model.create({
            'material_code': 'MAT003',
            'material_name': 'Old Material Name',
            'material_type': 'jeans',
            'material_buy_price': 200,
            'supplier_id': self.supplier.id,
        })
        material.write({'material_name': 'Updated Material Name'})
        self.assertEqual(material.material_name, 'Updated Material Name')

    def test_delete_material(self):
        material = self.material_model.create({
            'material_code': 'MAT004',
            'material_name': 'Deletable Material',
            'material_type': 'jeans',
            'material_buy_price': 150,
            'supplier_id': self.supplier.id,
        })
        material_id = material.id
        material.unlink()
        self.assertFalse(self.material_model.search([('id', '=', material_id)]))
