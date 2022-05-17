# -*- coding: utf-8 -*-

from odoo import models, fields, api


class help_desk_tag(models.Model):
    _name = 'help_desk.tag'

    name = fields.Char(string="Name")
