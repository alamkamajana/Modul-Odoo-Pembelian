import string
from odoo import fields, models


class DataBarang(models.Model):
    _name = 'data.barang'

    kode = fields.Char("Kode Barang")
    nama = fields.Char("Nama Barang")
    jumlah = fields.Integer("Jumlah Barang")
    harga = fields.Float("Harga Barang")

    
    









