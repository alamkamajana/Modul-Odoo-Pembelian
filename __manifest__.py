# -*- coding: utf-8 -*-
{
    'name': "Pembelian",

    'summary': """ 
    """,

    'tag': """
        Long tag of module's purpose
    """,

    'author': "",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/data_pembelian.xml',
        'views/data_barang.xml',
        'views/data_vendor.xml',
        'views/data_penjualan.xml'
        


    ],

}
