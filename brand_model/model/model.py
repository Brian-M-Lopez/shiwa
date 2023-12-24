from odoo import models, fields, _


class ModelBrand(models.Model):
    _name = "brand.model"

    name = fields.Char(string="Model name")
    brand = fields.Many2one(comodel_name="product.brand", string="Brand's model")