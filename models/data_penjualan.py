import string
from odoo import fields, models



class DataPenjualan(models.Model):
    _name = 'data.penjualan'

    kode = fields.Char("Kode Penjualan")
    barang = fields.Many2many("data.barang",string="Nama Barang")
    jumlah = fields.Char('jumlah')
    date = fields.Date("Tanggal Penjualan")
    
    









