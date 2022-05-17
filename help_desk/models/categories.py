# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_category(models.Model):
    _name = 'help_desk.category'

    name = fields.Char(string="Category Name")

