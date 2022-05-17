# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_sub_category(models.Model):
    _name = 'help_desk.sub_category'

    name = fields.Char(string="SubCategory Name")
    parent_category_ids = fields.Many2one('help_desk.category')

