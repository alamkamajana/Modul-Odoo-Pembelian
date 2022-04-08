# -*- coding: utf-8 -*-

import string
from odoo import fields, models


class DataPembelian(models.Model):
    _name = 'data.pembelian'

    name = fields.Char("Nomor Pembelian")
    vendor = fields.Many2one("data.vendor",string = "Nama Vendor")
    barang = fields.Many2many('data.barang',string="Nama Barang")
    jumlah = fields.Integer("Jumlah Pembelian")
    date = fields.Date("Tanggal Pembelian")
    
    









