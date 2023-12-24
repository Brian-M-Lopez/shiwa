from odoo import models, fields, _


class BrandProduct(models.Model):
    _name = "product.brand"

    name = fields.Char(string="Brand name")