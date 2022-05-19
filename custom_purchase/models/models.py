# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_purchase(models.Model):
   _inherit = "purchase.order"

   currency_id = fields.Many2one('res.currency', string="Currency")
