{
    'name': "Pembelian",

    'summary': """ Modul Pembelian
    """,

    'tag': """
        Pembelian
    """,
    'author': "Alam",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/data_pembelian.xml',
        'views/data_barang.xml',
        'views/data_vendor.xml',
        'views/data_penjualan.xml'
    ],
}
