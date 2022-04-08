# -*- coding: utf-8 -*-

from odoo import fields, models


class Vendor(models.Model):
    _name = 'data.vendor'

    name =fields.Char("Nama Vendor")
    address = fields.Char("Alamat")
    contact = fields.Char(" No Telp ")
    









