# -*- coding: utf-8 -*-

{
    'name': 'Purchase order confirmation date visibility',
    'version': '1.0.1.1',
    'author':'Soft-integration',
    'category': 'Sales',
    'summary': 'Configure the visibility of Purchase order confirmation date',
    'description': "",
    'depends': [
        'purchase',
    ],
    'data': [
        'security/purchase_order_date_approve_visibility_security.xml',
        'views/purchase_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
