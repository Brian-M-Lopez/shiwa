from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = "product.product"

    brand = fields.Many2one(comodel_name="product.brand", string="Product's brand")
    model = fields.Many2one(comodel_name="brand.model", string="Brand's model")

    @api.onchange('brand')
    def _clean_model_field(self):
        if self.model:
            self.model = False


class ProductTemplate(models.Model):
    _inherit = "product.template"

    brand = fields.Many2one(comodel_name="product.brand", string="Product's brand")
    model = fields.Many2one(comodel_name="brand.model", string="Brand's model")

    @api.onchange('brand')
    def _clean_model_field(self):
        if self.model:
            self.model = False