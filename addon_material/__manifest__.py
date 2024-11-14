{
    'name': 'Addon Material',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Modul untuk melakukan registrasi material yang akan dijual',
    'author': 'Pangeran Christian',
    'depends': ['base', 'contacts'],
    'data': [
        'views/material_views.xml',
        'views/material_security.xml',
        'views/supplier_views.xml',
        'views/material_menu.xml',
    ],
    'installable': True,
    'application': False,
}