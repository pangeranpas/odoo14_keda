{
    'name': 'Addon Material',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Module for registering and managing materials for sale',
    'author': 'Pangeran Christian',
    'depends': ['base', 'contacts'],
    'data': [
        'views/material_views.xml',
        'views/material_menu.xml',
        'views/material_security.xml',
    ],
    'installable': True,
    'application': False,
}